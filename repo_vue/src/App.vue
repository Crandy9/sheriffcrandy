<!-- navbar/footer template -->
<template>
  <div id="wrapper">
    <!-- header -->
    <header class="primary-header flex">
      <!-- logo on navbar-->
      <div class="logo">
        <router-link to="/">
          <strong>Sheriff Crandy</strong>
        </router-link>
      </div>
      <!-- hamburger button -->
      <button @click="navmenu" class="mobile-nav-toggle" aria-controls="primary-navigation" aria-expanded="false">
        <span class="sr-only">Menu</span>
      </button>

      <!-- responsive navbar -->
      <nav>
        <!-- data-visible used by nav.js -->
        <ul id="primary-navigation" data-visible="false"  class="primary-navigation flex">
          <li class="active">
            <router-link to="/">
              <span aria-hidden="true"></span>Home
            </router-link>
          </li>
          <li class="active">
            <router-link to="/about">
              <span aria-hidden="true"></span>Bio
            </router-link>
          </li>
          <li class="active">
            <router-link to="/signin">
              <span aria-hidden="true"></span>Sign in
            </router-link>
          </li>
          <li class="active">
            <router-link to="/contact">
              <span aria-hidden="true"></span>Contact
            </router-link>
          </li>
        </ul>
      </nav>
    </header>

    
    <!-- main page content -->
    <section class="section">
      <router-view/>
    </section>
		<!-- Footer -->
		<footer class="my-footer">
			<div class="footer_text" style="font-size: small;">
				<!-- Add styling from .net web app -->
				<div>
					&copy;
					2022 - Developed by
						<a class="company_link"
								href="https://lctechnologies.azurewebsites.net/" target="_blank">
							LC Technologies
							<img type="image/png" src="../src/assets/images/lctec_icon.jpg" alt="" width="15px" height="15px">
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
<script setup>

function navmenu() {
  const primaryNav = document.querySelector('.primary-navigation');
  const navToggle = document.querySelector('.mobile-nav-toggle');
  const visibility = primaryNav.getAttribute('data-visible');   

  if (visibility === "false") {
    primaryNav.setAttribute('data-visible', true);
    navToggle.setAttribute('aria-expanded', true);
  }
  else if (visibility === "true") {
    primaryNav.setAttribute('data-visible', false);
    navToggle.setAttribute('aria-expanded', false);

  }
}
</script>