<template>
    <div class="motordelenpage">
        <div class="row justify-content-center">
            <div class="col-10">
                <div class="breadcrumbs">
                    <ul class="breadcrumb">
                        <li><a href="/"><font-awesome-icon icon="home" /></a></li>
                        <li><a href="#">{selected moped}</a></li>
                        <li>Motordelen</li>
                    </ul>
                    <hr class="breadcrumbs-line">
                </div>
                <div class="row">
                    <div class="picture-selected-moped col-2">
                        <img class="img-fluid" src="img/icon/aerox_sideview-removebg-preview.png" alt="Moped" max-width="100%" height="auto">
                    </div>
                    <div class="info-selected-moped col-10">
                        <div class="row">
                            <h2>Yamaha Aerox 50 R (na 2003)</h2>
                        </div>
                        <div class="row">
                            <p>{The Aerox is built since 1997. The first generation was completely - precise manufacturing, robust build, easy maintainance and sporty modern design. A big advantage of the Yamaha Aerox / MBK Nitro with its common and widespread Minarelli horizontal LC engine is that it can be tuned easily, even inexperienced scooter owners can get a bit more power out of their scooter with simple, inexpensive parts and little know-how.}</p>
                        </div>
                    </div>
                </div>
                <kits />
                <motordelen />
                <framedelen />
                <mechanischedelen />
                <universeledelen />
                <nonscooter />
            </div>
        </div>
    </div>
</template>

<style>

/*---- begin breadcrumbs ----*/

/* Style the list */
ul.breadcrumb {
    padding: 10px 16px;
    list-style: none;
    margin-bottom: 0;
}

/* Display list items side by side */
ul.breadcrumb li {
    display: inline;
    font-size: 18px;
}

/* Add a slash symbol (/) before/behind each list item */
ul.breadcrumb li+li:before {
    padding: 8px;
    color: black;
    content: "›";
}

/* Add a color to all links inside the list */
ul.breadcrumb li a {
    color: #2c3e50;
    text-decoration: none;
    font-weight: 500;
}

/* Add a color on mouse-over */
ul.breadcrumb li a:hover {
    color: #025cac;
}

.breadcrumbs-line {
    height: 1px !important;
    border-width: 0;
    color: #c0c0c0;
    background-color: #c0c0c0;
    opacity: 1;
    margin: 0;
    margin-bottom: 30px;
}

/*---- end breadcrumbs ----*/

.currentpage {
    margin-bottom: 40px;
}

.picture-selected-moped {
    text-align: left;
}

.info-selected-moped {
    text-align: left;
}

.info-selected-moped p {
    font-size: 1.1vw;
}
</style>

<script>
import Navbar from "/src/components/navigationbar.vue"
import Footer from "/src/components/footerbar.vue"
import PageNav from "/src/components/navigation/pagenav.vue"
import motordelen from "/src/components/navigation/motordelen.vue"
import framedelen from "/src/components/navigation/framedelen.vue"
import mechanischedelen from "/src/components/navigation/mechanischedelen.vue"
import universeledelen from "/src/components/navigation/universeledelen.vue"
import kits from "/src/components/navigation/kits.vue"
import nonscooter from "/src/components/navigation/nonscooter.vue"

export default {
  name: 'Kits',
  components: {
    Navbar,
    Footer,
    PageNav,
    motordelen,
    framedelen,
    mechanischedelen,
    universeledelen,
    kits,
    nonscooter
  }
}
</script>