<!-- navbar/footer template -->
<template>
  <div id="wrapper">
      <!-- bulma navbar -->
      <nav class="navbar" role="navigation" aria-label="main navigation">
        <!-- logo on navbar-->
        <!-- <div class="navbar-brand"> -->
        <div class="navbar-brand">
          <router-link to="/" class="logo">
            <strong>Sheriff Crandy</strong>
            <!-- <span class="icon"><i class="fas fa-home"></i></span> -->
          </router-link>
          <!-- hamburger menu for mobile -->
          <!-- @click will change boolean to determine if menu is showed or not: false if true and true if false -->
          <a @click="showMobileMenu = !showMobileMenu" role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" v-bind:class="{'is-active':showMobileMenu}">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>
        <!-- navbar items -->
        <!-- v-bind is view directive which puts "is-active" next to navbar-menu class name. Used to control the nav items -->
        <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active':showMobileMenu}">
          <!-- make hamburger at right side of navbar -->
          <div class="navbar-end">
            <!-- navbar items -->
            <router-link to="/" class="navbar-item">Home</router-link>
            <router-link to="/music" class="navbar-item">Music</router-link>
            <router-link to="/tools" class="navbar-item">Tools I Use</router-link>
            <router-link to="/bio" class="navbar-item">Bio</router-link>
            <router-link to="/contact" class="navbar-item">Contact</router-link>
            <router-link to="/login" class="navbar-item">Log in</router-link>

            <div class="navbar-item">
              <div class="buttons">
                <router-link to="/cart" class="button is-success">
                  <!-- shopping cart icon -->
                  <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                  <span>Cart</span>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </nav>
        <!-- end bulma navbar -->

    
    <!-- main page content -->
    <section class="section">
      <router-view/>
    </section>
		<!-- Footer -->
		<footer class="my-footer">
			<div class="footer_text" style="font-size: small; padding: 1rem;">
				<!-- Add styling from .net web app -->
				<div>
					&copy;
					2023 - Developed by
						<a class="company_link"
								href="https://lctechnologies.azurewebsites.net/" target="_blank">
							LC Technologies
							<img class="footer-img" type="image/png" src="../src/assets/images/lctec_icon.jpg">
						</a> 				
						- Jesus Christ is King
				</div>
			</div>
		</footer>
		<!-- end Footer -->
  </div>
</template>

<!-- import bulma -->
<style lang="scss">
  @import '../node_modules/bulma';
</style>
<!-- import custom css file -->
<style>
  @import '../src/assets/styles/index.css';
</style>

<!-- hamburger menu animation -->
<script>
// open/close hamburger menu
export default {
  data () {
    return {
      showMobileMenu: false
    }
  },
  // close menu when nav link is clicked
  watch: {
    '$route' () {
      this.showMobileMenu = false
    }
  }
}
</script> 