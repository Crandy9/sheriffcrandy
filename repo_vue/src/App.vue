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
      <!-- SNS icons -->
      <div class="social-media-div">
        <ul class="sns">
          <li class="instagram">
              <a 
                class="icon instagram" 
                rel="noopener" 
                target="_blank" 
                title="https://www.instagram.com/sheriffcrandy/"
                href="https://www.instagram.com/sheriffcrandy/">
                <svg
                  xmlns="http://www.w3.org/2000/svg" 
                  viewBox="0 0 18 18" 
                  class="icon">
                  <path 
                    fill-rule="evenodd" 
                    d="M6.955 1.628l2.582-.006c1.916.001 2.227.012 3.1.052.877.04 1.354.187 1.67.31.421.163.72.358 1.036.673.27.27.452.529.6.862l.073.173c.113.29.246.715.298 1.46l.03.627c.012.29.02.553.025.917l.01 2.842c-.002 1.915-.013 2.226-.053 3.099-.037.804-.163 1.272-.279 1.588l-.031.083c-.163.42-.358.72-.673 1.035-.315.315-.615.51-1.035.673-.29.113-.715.246-1.46.298l-1.21.05c-.344.007-.761.011-1.428.013l-3.255-.005a37.01 37.01 0 01-1.592-.046c-.877-.04-1.354-.187-1.67-.31a2.788 2.788 0 01-1.036-.673 2.788 2.788 0 01-.673-1.035c-.113-.29-.246-.715-.298-1.46l-.05-1.21a71.292 71.292 0 01-.013-1.428l.005-3.255c.006-.692.02-1.022.046-1.592.04-.877.187-1.354.31-1.67.163-.421.358-.72.673-1.036.315-.315.615-.51 1.035-.673.29-.113.715-.246 1.46-.298l.627-.03c.355-.015.668-.023 1.176-.028zM6.97.006h4.06c.747.007 1.09.021 1.68.048.959.044 1.613.196 2.185.419.592.23 1.094.537 1.594 1.038.5.5.808 1.002 1.038 1.594.198.509.34 1.082.4 1.876l.035.68c.026.62.036 1.093.038 2.574l-.005 2.658c-.006.844-.02 1.192-.05 1.818-.043.958-.195 1.612-.418 2.184a4.412 4.412 0 01-1.038 1.594c-.5.5-1.002.809-1.594 1.039-.509.197-1.082.34-1.876.4l-.795.039c-.53.021-1.003.03-2.193.032l-2.924-.004a39.115 39.115 0 01-1.818-.05c-.958-.043-1.612-.195-2.184-.417a4.412 4.412 0 01-1.594-1.039c-.5-.5-.809-1.002-1.039-1.594-.197-.509-.34-1.082-.4-1.876l-.042-.876C.009 11.575 0 11.027 0 9.527L.006 6.97c.007-.747.021-1.09.048-1.68.044-.959.196-1.613.418-2.185A4.412 4.412 0 011.511 1.51c.5-.5 1.002-.808 1.594-1.038.509-.198 1.082-.34 1.876-.4L5.857.03C6.177.018 6.49.01 6.97.006zm2.048 4.387a4.625 4.625 0 100 9.25 4.625 4.625 0 000-9.25zm0 1.623a3.002 3.002 0 110 6.004 3.002 3.002 0 010-6.004zm4.768-2.909a1.071 1.071 0 100 2.143 1.071 1.071 0 000-2.143z">
                  </path>
                </svg>
              </a>
          </li>
          <li class="youtube">
              <a 
                class="icon youtube" 
                rel="noopener" 
                target="_blank" 
                title="https://www.youtube.com/@sheriffcrandy"
                href="https://www.youtube.com/@sheriffcrandy">
                <svg 
                  xmlns="http://www.w3.org/2000/svg" 
                  viewBox="0 0 18 14" 
                  class="icon">
                  <path 
                    d="M7.518.011l1.81-.01c.971.004 3.89.03 5.972.173l.355.05c.394.061.95.209 1.445.76.463.478.66 1.426.714 1.746l.017.108s.155 1.378.168 2.816L18 7.241c0 .654-.032 1.31-.068 1.84l-.1 1.172s-.17 1.274-.732 1.853c-.675.753-1.463.753-1.8.811l-.537.033c-2.11.12-4.778.138-5.547.14l-2.132-.03c-1.465-.029-3.372-.076-4.215-.143-.394-.116-1.294-.058-1.969-.81-.43-.444-.63-1.293-.7-1.668l-.031-.186S.014 8.875 0 7.437V5.654l.007-.39c.012-.45.035-.883.06-1.254l.1-1.172S.339 1.564.9.985C1.575.232 2.362.232 2.7.174l.75-.045C4.827.057 6.4.025 7.518.01zm-.973 3.262v6.545l6.546-3.273-6.546-3.272z">
                  </path>
                </svg>
              </a>
          </li>
          <li class="twitter">
              <a 
                class="icon twitter" 
                rel="noopener" 
                target="_blank" 
                title="https://twitter.com/sheriffcrandy"
                href="https://twitter.com/sheriffcrandy">
                <svg 
                  xmlns="http://www.w3.org/2000/svg" 
                  viewBox="0 0 18 16" 
                  class="icon">
                  <path 
                    fill-rule="evenodd" 
                    d="M15.88 2.44A3.866 3.866 0 0017.502.284a7.162 7.162 0 01-2.345.945A3.595 3.595 0 0012.462 0C10.422 0 8.77 1.744 8.77 3.894c0 .306.03.603.094.887C5.796 4.62 3.076 3.07 1.253.712a4.05 4.05 0 00-.5 1.959c0 1.35.652 2.543 1.643 3.243a3.56 3.56 0 01-1.673-.487v.048c0 1.887 1.272 3.462 2.963 3.818-.31.092-.636.137-.974.137-.238 0-.47-.023-.694-.069.47 1.547 1.833 2.675 3.45 2.705A7.17 7.17 0 010 13.679a10.07 10.07 0 005.66 1.75c6.794 0 10.507-5.935 10.507-11.082 0-.17-.002-.338-.01-.504A7.72 7.72 0 0018 1.826c-.662.31-1.375.52-2.12.613z">
                  </path>
                </svg>
              </a>
          </li>
        </ul>
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