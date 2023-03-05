<template>
  <div class="home">
    <div class="firstpartbody">
      <div class="row errorrow">
        <div class="mainimage col-8">
          <!-- <img src="img/icon/vespatest3.jpg" alt="aerox" width="100%" height="600px"> -->
          <video loop autoplay muted class="videoInsert">
            <source src="video/stunt_AdobeExpress.mp4" type="video/mp4">
            <!-- <source src="video/stunt.ogg" type="video/ogg"> -->
            Your browser does not support the video tag.
          </video>
        </div>
        <div class="sidecolumn col-4">
          <div class="sidecolumndiv">
            <div class="container p-4">
              <div class="firstrow row">
                <p>parts</p>
              </div>
              <div class="secondrow row">
                <h1>outlet</h1>
              </div>
              <div class="thirdrow row">
                <div class="shopnubutton col-6">
                  <button type="button" class="motordelenbutton btn-lg btn-danger">Motordelen</button>
                </div>
                <div class="letmeshopbutton col-6">
                  <button type="button" class="framedelenbuttonwidth btn-lg btn-outline-secondary">Framedelen</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="secondpartbody">
      <div class="row justify-content-center">
        <div class="maintenancecolumn col-3"></div>
        <div class="spacebetween col-1"></div>
        <div class="kitscolumn col-3"></div>
        <div class="spacebetween col-1"></div>
        <div class="racingproductencolumn col-3"></div>
      </div>
    </div>
    <div class="seperatiesegment">
      <div class="row justify-content-center">
        <div class="spacebegin col-1"></div>
        <div class="checkbox_list col">
          <ul class="list-group list-group-horizontal">
            <li class="list-group-item flex-fill"><font-awesome-icon icon="wallet" :style="{ color: '#2c3e50', width: '18px', height: '18px', marginRight: '5px'}"/>Laagste prijsgarantie</li>
            <li class="list-group-item flex-fill"><font-awesome-icon icon="bolt" :style="{ color: '#2c3e50', width: '18px', height: '18px', marginRight: '5px'}"/>Snelle levering</li>
            <li class="list-group-item flex-fill"><font-awesome-icon icon="truck" :style="{ color: '#2c3e50', width: '18px', height: '18px', marginRight: '5px'}"/>Gratis verzending</li>
            <li class="list-group-item flex-fill"><font-awesome-icon icon="clock" :style="{ color: '#2c3e50', width: '18px', height: '18px', marginRight: '5px'}"/>retourneren tot 60 dagen</li>
            <li class="list-group-item flex-fill"><font-awesome-icon icon="phone" :style="{ color: '#2c3e50', width: '18px', height: '18px', marginRight: '5px'}"/>altijd bereikbaar</li>
          </ul>
        </div>
        <div class="spaceend col-1"></div>
      </div>
    </div>
    <div class="thirdpartbody">
      <div class="row justify-content-center">
        <div class="col-11">
          <div class="row outline">
            <div class="enginecolumn col-6">
              <p>motor onderdelen</p>
              <button type="button" class="framedelenbutton btn btn-outline-secondary">Shop nu</button>
              <!-- <img src="img/engine.jpg" alt="motordelen" class="fit-image-home"> -->
            </div>
            <div class="framecolumn col-6">
              <p>frame onderdelen</p>
              <button type="button" class="framedelenbutton btn btn-outline-secondary">Shop nu</button>
            </div>
          </div>
          <div class="row outline">
            <div class="mechanicalcolumn col-6">
              <p>mechanische onderdelen</p>
              <button type="button" class="framedelenbutton btn btn-outline-secondary">Shop nu</button>
            </div>
            <div class="universalcolumn col-6">
              <p>universele onderdelen</p>
              <button type="button" class="framedelenbutton btn btn-outline-secondary">Shop nu</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap');

h1, h2, h3, h4, p, a {
  font-family: "Roboto", sans-serif;
}

ul {
  list-style-type: none;
}

.home {
  background-color: #F0F1F2;
}

.row {
  margin-right: 0px!important;
}

.sidecolumndiv {
  height: 300px;
  background-color: white;
  margin-left: -25%;
  margin-top: 15%;
}

.mainimage, .sidecolumn {
  padding: 0px!important;
}

.errorrow {
  margin-right: 0px!important;
  margin-left: 0px!important;
}

.firstrow { 
  text-align: left;
  font-size: 25px;
  letter-spacing: 1em;
  margin-top: 2rem!important;
}

.firstrow p {
  margin-bottom: 0px;
}

.secondrow {
  text-align: left;
}

.secondrow h1 {
  font-weight: 900;
  font-size: 60px;
}

.thirdrow {
  text-align: left;
}

.motordelenbutton {
  background-color: #ec2d0f!important;
  border: none;
  width: 50%;
  height: 100%;
}

.motordelenbutton:hover {
  background-color: #cc3821!important;
}

.framedelenbuttonwidth {
  width: 50%;
}

.framedelenbutton, .framedelenbuttonwidth {
  /* background-color: white!important;
  border: 1px solid #676767;
  width: 50%;
  color: rgb(53, 53, 53)!important; */
  border: 1.5px solid;
  background-color: white;
  color: #2c3e50!important;
}

.framedelenbutton:hover, .framedelenbuttonwidth:hover {
  color: white!important;
}



.secondpartbody {
  margin-top: 100px;
}

.maintenancecolumn, .kitscolumn, .racingproductencolumn {
  width: 100%;
  height: 400px;
  border: 1px solid rgb(53, 53, 53);
}



.seperatiesegment {
  margin-top: 50px;
  margin-bottom: 50px;
}

.checkbox_list {
  display: inline;
  text-decoration: none;
}

.list-group-item {
  background-color: #F0F1F2!important;;
  border: none!important;
}

.enginecolumn, .framecolumn, .mechanicalcolumn, .universalcolumn {
  border: 1px solid black;
  height: 450px;
}

.enginecolumn p, .framecolumn p, .mechanicalcolumn p, .universalcolumn p {
  margin-top: 20%;
}

.videoInsert {
  /* position: absolute;  */
  right: 0; 
  bottom: 0;
  min-width: 100%; 
  min-height: 100%;
  width: auto; 
  height: auto; 
  /* z-index: -100; */
  background-size: cover;
  overflow: hidden;
}

.fit-image-home {
  width: 100%;
  height: auto;
}
</style>

<script>
import Navbar from "../components/navigationbar.vue"
import Footer from "../components/footerbar.vue"

export default {
  name: 'Home',
  components: {
    Navbar,
    Footer
  },
  mounted() {
    document.title = '24stroke'
  }
}
</script>
