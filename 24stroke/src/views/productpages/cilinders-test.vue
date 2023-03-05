<template>
    <div class="cilinders-product-page">
        <div class="row justify-content-center">
            <div class="col-10">
                <div class="breadcrumbs">
                    <ul class="breadcrumb">
                        <li><a href="/"><font-awesome-icon icon="home" /></a></li>
                        <li><a href="#">{selected moped}</a></li>
                        <li><a href="/motordelen">Motordelen</a></li>
                        <li>Cilinders</li>
                    </ul>
                    <hr class="breadcrumbs-line">
                </div>
                <div class="row">
                    <div class="col-2">
                        <div class="row justify-content-left">
                            <div class="col-11 product-filter px-3">
                                <div v-for="technical_detail in technical_details" :key="technical_detail">
                                    <ProductFilter :technical_detail="technical_detail" :filters="filters" v-on:filterclick="filtercall($event)"/>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-10">
                        <topInformation :results="products.length" />
                        <div class="row products-row">
                            <ProductBox  v-for="product in products" :key="product.id" v-bind:product="product" />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
.product-filter {
    background-color: white;
    border-radius: 4px;
}
</style>


<script>
import axios from 'axios'

import topInformation from '../../components/topInformation.vue'
import ProductBox from '@/components/ProductBox'
import ProductFilter from '@/components/filter.vue'

export default {
  name: 'Category',
  components: {
    ProductBox,
    topInformation,
    ProductFilter
  },
  data() {
    return {
        products: {
      },
      technical_details: [],
      category_id: null,
      filters: []
    }
  },
  mounted() {
      this.getCategory()
      this.filters = this.$store.state.filters
  },
  watch: {
      $route(to, from) {
            this.getCategory()
      }
  },
  methods: {
      async getCategory() {
          const categorySlug = this.$route.params.category_slug

          this.$store.commit('setIsLoading', true)
          
          await axios
            .get(`api/v1/products/${categorySlug}/`)
            .then(response => {
                this.category_id = response.data.id
            })
            .catch(error => {
                console.log(error)
            })

            this.$store.commit('setIsLoading', false)
          

          if (this.filters.length > 0) {
            this.newFilteredProductCall()
          } else { 
            await axios
                .get(`api/v1/products/?category=${this.category_id}`)
                .then(response => {
                    this.products = response.data
                    this.available_filters(response.data, null)

                    document.title = "24stroke | " + this.category.name
                })
                .catch(error => {
                    console.log(error)
                })

                this.$store.commit('setIsLoading', false)
          }
      },
      available_filters(products, clickedFilter) {
        var temp_technical_details = []
        this.technical_details = this.$store.state.technicalDetails
        if (this.technical_details.length > 0 && clickedFilter !== null) {
            console.log(this.technical_details)
            var indexofclickedfilter = this.technical_details.map(e => e.name).indexOf((clickedFilter.charAt(0).toUpperCase() + clickedFilter.slice(1)).replace(/_/g," "))
            console.log(indexofclickedfilter)
            temp_technical_details.push(this.technical_details[indexofclickedfilter])
        }
        products.forEach(product => {
            //for each product check the technical details
            for (var propt in product.technical_details_dutch) {
                //for each technical detail, check if technical detail is not null or something we don't want as a filter
                if (product.technical_details_dutch[propt] !== null && propt !== 'id' && propt !== 'artikel_nummer' && propt !== 'ean' && propt !== 'naam' && propt !== clickedFilter) {
                    var alreadythere = false
                    //foreach technical detail, check if it's already in the array with non null technical-details
                    temp_technical_details.forEach(detail => {
                        if ((propt.charAt(0).toUpperCase() + propt.slice(1)).replace(/_/g," ") === detail.name) {
                            alreadythere = true
                            var addnewValue = true
                            //push to detail.value if detail.value.detail is not the same. Otherwise just increase the count of the specific detail.value.detail
                            detail.value.forEach(filter => {
                                if (filter.detail == product.technical_details_dutch[propt]) {
                                    console.log(filter)
                                    filter.count = filter.count + 1
                                    addnewValue = false
                                }
                            });
                            if (addnewValue) {
                                var value = {
                                    detail: product.technical_details_dutch[propt],
                                    count: 1,
                                    enabled: false
                                }
                                detail.value.push(value)
                            }
                            // detail.value.detail.push(product.technical_details[propt])
                            // detail.value.count = detail.value.count + 1
                        }
                    });
                    if (!alreadythere) {
                        var tempname = propt.charAt(0).toUpperCase() + propt.slice(1)
                        tempname = tempname.replace(/_/g," ")
                        var technical_detail_object = {
                            name: tempname,
                            value: [{
                                detail: product.technical_details_dutch[propt],
                                count: 1,
                                enabled: false
                            }]
                        }
                        temp_technical_details.push(technical_detail_object)
                    }
                }
            }
        });
        // var activefilter = this.technical_details.
        this.technical_details = this.filterSortByCount(temp_technical_details)
      },
      filtercall(filter) {
        // this.$store.commit('setIsLoading', true)
        this.$store.commit('addTechnicalDetails', this.technical_details)
        var filters = this.$store.state.filters
        var filtername = filter.name.charAt(0).toLowerCase() + filter.name.slice(1)
        filtername = filtername.replace(/ /g,"_")
        var storefilter = {
            name: filtername,
            filtering: [filter.filtering.detail]
        }

        if (filter.filtering.enabled == true) {
            var alreadyinstate = false
            filters.forEach(filterobject => {
                if (filterobject.name == filtername) {
                    //filter already exist, value needs to be added to the filtering under the same name
                    alreadyinstate = true
                    this.$store.commit('addFilterValue', [filterobject, filter.filtering.detail] )
                }
            });
            if (!alreadyinstate) {
                this.$store.commit('addFilter', storefilter)
            }
        }
        else if (filter.filtering.enabled == false) {
            //if theres 2 values and 1 name, remove only the value
            //otherwise remove the entire filter
            //then update all the items

            filters.forEach(filterobject => {
                if (filtername == filterobject.name) {
                    if (filterobject.filtering.length > 1){
                        this.$store.commit('removeFilterValue', [filterobject, storefilter])
                    }
                    else {
                        this.$store.commit('removeFilter', storefilter)
                    }
                }
            });
        }
        this.newFilteredProductCall()
        // this.$store.commit('setIsLoading', false)
      },
      async newFilteredProductCall() {
        var filtersUpdated = this.$store.state.filters
        var filterstring = ""
        filtersUpdated.forEach(filterobject => {
            filterstring = filterstring.concat("&technical_details_dutch__", filterobject.name) + "__in="
            for(var i = 0; i < filterobject.filtering.length; i++) {
                if (i == 0) {
                    filterstring = filterstring.concat("", filterobject.filtering[i])
                }
                else {
                    filterstring = filterstring.concat(",", filterobject.filtering[i])
                }
            };
        })

        await axios
        .get(`api/v1/products/?category=${this.category_id}${filterstring}`)
        .then(response => {
            this.products = response.data
            this.available_filters(response.data, 'merk')
            // this.available_filters(response.data)
        })
        .catch(error => {
            console.log(error)
        })
      },
      filterSortByCount(technical_details_object) {
        var unsorted_array = []
        technical_details_object.forEach(technical_detail => {
            // console.log(technical_detail)
            technical_detail.value.sort((a,b) => parseFloat(b.count) - parseFloat(a.count))
        //     technical_detail.forEach(value => {
        //         technical_detail.sort((a,b) => parseFloat(a.count) - parseFloat(b.count))
        // })
        })
        return technical_details_object
      },
  }
}
</script>