<template>

  <section class="main-music-section">

    <!-- music tracks -->
    <section class="title-art-sfsb-section">
      <!-- title -->
      <div class="column is-12" >
        <h2 class="music-title is-size-3 has-text-centered has-text-white">
          Sheriff Crandy Music
        </h2>
      </div>
      <div>
        <!-- show this if no songs have been playing -->
        <h3 v-if="$store.state.currentTrackPlaying == 0" style="padding: 1rem; font-size: 16px !important;" class="is-size-5 has-text-warning">
          {{$t('musicview.clicktohearsample')}}
        </h3>
      </div>
    </section>
    <section class="music-player-section">
      <!-- need to wrap the v-for div in a parent div to allow scrolling on div -->
      <!-- show track img for current track -->
      <!-- or leave title and track img up after song stops playing -->
      <!-- v-bind:key is used to optimize rendering -->
      <div class="parent-element" style="overflow: auto;">
        <div v-for="trackDisplay in tracks" v-bind:key="trackDisplay.id">
          <div class="track-cover-art-div" v-if="$store.state.currentTrackPlaying == trackDisplay.id" 
            :style="{ backgroundImage: 'url(' + trackDisplay.get_cover_art + ')' }"
            @contextmenu.prevent
            @touchmove.prevent
            style="-webkit-touch-callout: none; -webkit-user-select: none; -ms-touch-action: none; touch-action: none;">        
          </div>
          <h3 v-if="$store.state.currentTrackPlaying == trackDisplay.id" class="track-title-img">
            Sheriff Crandy - {{ trackDisplay.title }}
          </h3>
        </div>
      </div>
      <!-- skip, play/pause, repeat, shuffle controllers -->
      <div class="music-player-controls-wrapper">
        <div class="music-player-controls">
          <!-- repeat controller -->
          <span class="repeat-controller" 
          @click.prevent="toggleRepeat">
            <i class="fas fa-sync" :class="{ rotate: isRotated}"></i>
          </span>
          <!-- skip previous -->
          <span class="skip-back-controller" 
          @click.prevent="skipPreviousController()">
            <i class="fa fa-fast-backward"></i>
          </span>
          <!-- play controller showing when paused -->
          <span class="play-controller" v-if="!$store.state.currentAudioElementPlaying" 
          @click.prevent="playPauseController()">
            <i class="fas fa-play"></i>          
          </span>
          <!-- pause controller shown when playing -->
          <span class="pause-controller" v-if="$store.state.currentAudioElementPlaying" @click.prevent="playPauseController()">
            <i class="fas fa-pause"></i>          
          </span>
          <!-- skip forward -->
          <span class="skip-forward-controller" 
          @click.prevent="skipForwardController()">
            <i class="fa fa-fast-forward"></i>  
          </span>
          <span class="shuffle-controller" 
          @click.prevent="toggleShuffle">
            <i class="fas fa-random" :class="{ invert: isInverted}"></i>
          </span>
        </div>
      </div>
      <div class="slider-container">
        <!-- slide bar -->
        <div class="slide-bar" ref="slideBar" id="slideBar" 
          @mousedown="sliderMoveDesktop"
          @touchstart="sliderMoveMobile"
          @mouseover="$store.state.isSlidebarHovering = true, updateSlideBarBackground"
          @mouseleave="$store.state.isSlidebarHovering = false, updateSlideBarBackground">
          <div 
            class="slider" 
            ref="slider" 
            id="slider" 
            :style="{ left: $store.state.progress + '%'}">
          </div>
        </div>
        <div class="track-time-displays">
          <span class="start-time">
            {{ $store.state.songProgress }}
          </span>
          <span v-show="$store.state.songLength" class="end-time">
            {{$store.state.songLength}}
          </span>
        </div>
      </div>
      <!-- currently playing song -->
      <!-- unordered list of track -->
      <ul class="audio-player-ul">
        <!-- Vue for loop -->
        <div v-for="track, index in tracks" v-bind:key="track.id" class="media-player">
          <li @click="setPlayOrPause(track.id)" class="track-list-item" v-bind:id="track.id">
            <!-- show play button on all tracks on hover -->
            <a class="play-button" href="#" v-if="$store.state.currentTrackPlaying != track.id"> 
              <span class="play-icon-span">
                <svg 
                  class="play-icon-svg" 
                  xmlns="http://www.w3.org/2000/svg" 
                  preserveAspectRatio="xMinYMin meet"
                  viewBox="0 0 26 26">
                  <polygon points="9.33 6.69 9.33 19.39 19.3 13.04 9.33 6.69" />
                </svg>
              </span>
            </a>
            <!-- show play button on paused track -->
            <a class="play-button-on-pause" href="#"
              v-if="$store.state.currentTrackPlaying == track.id && $store.state.currentAudioElementPlaying == false">
              <span class="play-icon-span">
                <svg 
                  class="play-icon-svg" 
                  xmlns="http://www.w3.org/2000/svg" 
                  preserveAspectRatio="xMinYMin meet"
                  viewBox="0 0 26 26">
                  <polygon points="9.33 6.69 9.33 19.39 19.3 13.04 9.33 6.69" />
                </svg>
              </span>
            </a>
            <!-- show pause button while playing -->
            <a class="pause-button" href="#" v-if="$store.state.currentTrackPlaying == track.id && $store.state.currentAudioElementPlaying == true">
              <!-- show pause button only on track that is currently playing -->
              <span class="pause-icon-span" style="display: block !important">
                <svg 
                  class="pause-icon-svg" 
                  xmlns="http://www.w3.org/2000/svg" 
                  preserveAspectRatio="xMinYMin meet"
                  viewBox="0 0 16 16">
                  <path
                    d="M6 3.5 a.5.5 0 0 1 .5.5v8a.5.5 0 0 1-1 0V4a.5.5 0 0 1 .5-.5zm4 0a.5.5 0 0 1 .5.5v8a.5.5 0 0 1-1 0V4a.5.5 0 0 1 .5-.5z">
                  </path>
                </svg>
              </span>
            </a>
            <!-- hide track number when track is playing -->
            <span v-if="$store.state.currentTrackPlaying != track.id" class="track-number">{{++index}}</span>
            <!-- track title -->
            <div class="track-title">
              <span class="track-title-inner">
                {{ track.title }}
                <span class="track-dur">
                  {{ track.get_track_duration }}
                </span>
              </span>
            </div>
            <!-- price -->
            <div class="field has-addons">
              <!-- had to change class name because 'control' was being used by login/signup forms -->
              <div class="sheriff-crandy-music-ctrl-panel">
                <!-- check if this item is already in the cart -->
                <a class="music-in-cart-button button is-small price-button has-text-weight-medium" 
                  v-if="checkIfTrackIsInCart(track)" 
                  @click.stop="modalOpened = false; removeFromCart(track.id)" data-target="my-modal-id">
                  {{$t('cartview.addedtocart')}}
                </a>
                <!-- open modal. click.stop prevents the parent click even from firing.
                  Doesn't play/pause the song, adds this item to cart only
                -->
                <a class="button is-small is-black price-button has-text-weight-medium" 
                  v-else-if="track.is_free" 
                  @click.stop="modalOpened = true; setTrack(track.id);" data-target="my-modal-id">
                  {{$t('cartview.free')}}

                </a>
                <a class="button is-small is-black price-button has-text-weight-medium" 
                  v-else-if="track.usd_price && $store.state.region === 'US'"
                  @click.stop="modalOpened = true; setTrack(track.id);" data-target="my-modal-id">
                  ${{ track.usd_price }}
                </a>
                <a class="button is-small is-black price-button has-text-weight-medium" 
                  v-else-if="track.usd_price && $store.state.region === 'JP'"
                  @click.stop="modalOpened = true; setTrack(track.id);" data-target="my-modal-id">
                  ¥{{ track.jpy_price }}
                </a>
              </div>
            </div>
          </li>
        </div>
      </ul>
    </section>
    <!-- modal -->
    <Transition>
      <div v-if="modalOpened" id="my-modal-id" class="modal" v-bind:class="{'is-active':modalOpened}">
        <div class="modal-background"></div>
          <div class="modal-card">
            <header class="modal-card-head">
              <p v-if="isFree" class="modal-card-title">{{$t('cartview.downloadnow?')}}</p>
              <p v-else class="modal-card-title">{{$t('cartview.buynow?')}}</p>
              <button @click="modalOpened = false" class="delete" aria-label="close"></button>
            </header>
            <!-- free US -->
            <section v-if="isFree && $store.state.language === 'en'" class="modal-card-body">
              {{$t('cartview.doyouwannadownload?part1')}}"{{ setTrackTitle }}" {{$t('cartview.doyouwannadownload?part2')}}
            </section>
            <!-- free JA -->
            <section v-else-if="isFree && $store.state.language === 'ja'" class="modal-card-body">
              "{{ setTrackTitle }}" {{$t('cartview.doyouwannadownload?part1')}}
            </section>
            <!-- purchase US -->
            <section v-else-if="$store.state.language === 'en'" class="modal-card-body">
              {{$t('cartview.doyouwannabuy?part1')}}"{{ setTrackTitle }}" {{$t('cartview.doyouwannabuy?part2')}}
            </section>
            <!-- purchase JA -->
            <section v-else-if="$store.state.language === 'ja'" class="modal-card-body">
              "{{ setTrackTitle }}"{{$t('cartview.doyouwannabuy?part1')}}
            </section>
            <footer class="modal-card-foot">
              <div v-if="$store.state.isAuthenticated">
                <button v-if="isFree" @click="modalOpened = false; show = false; purchaseButtonClicked = false; downloadFreeNow(setTrackTitle, setTrackID);" class="my-modal-button-buy-now button">{{$t('cartview.downloadnow')}}</button>
                <!-- trigger stripe payment on this item only -->
                <button v-else @click="modalOpened = false; show = true; purchaseButtonClicked = true; buyNow(); scrollToBottom();" class="my-modal-button-buy-now button">{{$t('cartview.buynow')}}</button>
                <!-- if adding to cart, add the item to cart and close modal -->
                <button @click.stop="addTrackToCart(setTrackID); modalOpened = false" class="my-modal-button-add-to-cart button">{{$t('cartview.addtocart')}}</button>
              </div>
              <!-- if user is not logged in, redirect to login screen -->
              <div v-else>
                <!-- pass in the flpname of the free flp to be downloaded -->
                <a v-if="isFree" role="button" @click='redirectToLogin()' class="my-modal-button-buy-now button">{{$t('cartview.downloadnow')}}</a>
                <!-- trigger stripe payment on this item only -->
                <a v-else role="button" @click='redirectToLogin()' class="my-modal-button-buy-now button">{{$t('cartview.buynow')}}</a>
                <!-- if adding to cart, add the item to cart and close modal -->
                <a role="button" @click='redirectToLogin()' class="my-modal-button-add-to-cart button">{{$t('cartview.addtocart')}}</a>
              </div>
            </footer>
          </div>
      </div>
    </Transition>
    <h2 class="music-guide has-text-centered has-text-warning">
      {{$t('musicview.about')}}
      <div class="is-size-6" style="padding: 1rem;">
        <p style="padding:1.2rem;">
          <a class="file-links" target="blank" href="https://www.wideanglesoftware.com/blog/how-to-transfer-music-from-computer-to-android.php#:~:text=on%20your%20Mac.-,Connect%20your%20Android%20to%20your%20Windows%20PC%20using%20a%20USB,device%20in%20Android%20File%20Transfer.">
            {{$t('musicview.cputoandroid')}}
          </a>
        </p>
        <p style="padding:1.2rem;">
          <a class="file-links" target="blank" href="https://support.apple.com/guide/itunes/transfer-files-itns32636/windows">
            {{$t('musicview.cputoiphone')}}
          </a>
        </p>
      </div>
    </h2>
  </section>
  <!-- FOR BUY NOW -->
  <!-- stripe payment form copied from cart view -->
    <div style="z-index: 9999;" class="my-checkout-div"
      :style="showPaymentForm()" v-bind:class="{'is-active': purchaseButtonClicked}" ref="paymentFormTop">
        <!-- <div class="modal-background"></div> -->
          <div class="card">
            <header class="card-head">
              <!-- <p class="card-title">{{$t('paymentmodal.modaltitle')}}</p> -->
              <button class="delete close-button" @click="show = false; clearFields(); purchaseButtonClicked = false;" aria-label="close"></button>
            </header>
            <section class="card-body">
              <div class="page-checkout">
                <div class="columns is-multiline">
                    <div class="column is-12 box">
                      <h2 style= "text-align: center;" class="payment-form-sub subtitle has-text-black has-text-center is-underlined">{{$t('paymentmodal.paymentdetails')}}</h2>
                      <h2 class="subtitle has-text-black">{{$t('paymentmodal.billingaddress')}}</h2>
                      <!-- <p class="has-text-danger mb-4">* All fields are required</p> -->
                      <div class="columns is-multiline">
                        <div class="column is-6">
                          <!-- name errors-->
                          <div v-if="errors.nameErrors.length">
                              <p class="my-errors" style="color:red" v-for="error in errors.nameErrors" v-bind:key="error">
                              <span style="color:red !important">*</span> {{ error }}
                              </p>                        
                          </div>
                          <div class="field">
                            <label class="my-label has-text-black">{{$t('paymentmodal.name')}}</label>
                            <div class="control">
                                <input type="text" class="input" :placeholder="$t('paymentmodal.placeholdername')" v-model="name">
                            </div>
                          </div>
                          <!-- email errors-->
                          <div v-if="errors.emailErrors.length">
                              <p class="my-errors" style="color:red" v-for="error in errors.emailErrors" v-bind:key="error">
                              <span style="color:red !important">*</span> {{ error }}
                              </p>                        
                          </div>
                          <div class="field">
                            <label class="my-label has-text-black">{{$t('paymentmodal.email')}}</label>
                            <div class="control">
                                <input type="email" class="input" placeholder="123@my-email.com" v-model="email">
                            </div>
                          </div>
                          <!-- phone errors-->
                          <div v-if="errors.phoneErrors.length">
                              <p class="my-errors" style="color:red" v-for="error in errors.phoneErrors" v-bind:key="error">
                              <span style="color:red !important">*</span> {{ error }}
                              </p>                        
                          </div>
                          <div class="field">
                            <label class="my-label has-text-black">{{$t('paymentmodal.phone')}}</label>
                            <div class="control">
                                <input type="text" class="input" :placeholder="$t('paymentmodal.placeholderphone')" v-model="phone">
                            </div>
                          </div>
                          <!-- address1 errors-->
                          <div v-if="errors.address1Errors.length">
                              <p class="my-errors" style="color:red" v-for="error in errors.address1Errors" v-bind:key="error">
                              <span style="color:red !important">*</span> {{ error }}
                              </p>                        
                          </div>
                          <div class="field">
                            <label class="my-label has-text-black">{{$t('paymentmodal.street1')}}</label>
                            <div class="control">
                                <input type="text" class="input" :placeholder="$t('paymentmodal.street1placeholder')" v-model="address1">
                            </div>
                          </div>
                            <!-- address2 errors-->
                            <div v-if="errors.address2Errors.length">
                              <p class="my-errors" style="color:red" v-for="error in errors.address2Errors" v-bind:key="error">
                              <span style="color:red !important">*</span> {{ error }}
                              </p>                        
                          </div>
                          <div class="field">
                            <label class="my-label has-text-black">{{$t('paymentmodal.street2')}}</label>
                            <div class="control">
                                <input type="text" class="input" :placeholder="$t('paymentmodal.street2placeholder')"  v-model="address2">
                            </div>
                          </div>
                        </div>
                        <div class="column is-6">
                            <!-- country errors-->
                            <div v-if="errors.countryErrors.length">
                              <p class="my-errors" style="color:red" v-for="error in errors.countryErrors" v-bind:key="error">
                              <span style="color:red !important">*</span> {{ error }}
                              </p>                        
                            </div>
                            <div class="field">
                              <label class="my-label has-text-black">{{$t('paymentmodal.country')}}</label>
                              <div class="control has-icons-left">
                                  <select class="input" v-model="country" name="country" id="id_country">
                                    <option style="color:rgba(0,0,0,0.4) !important" value="" disabled selected hidden>
                                        {{$t('paymentmodal.countryplaceholder')}}
                                    </option>
                                    <option v-for="cya in $store.state.countries" :value="cya.countryval" style="color: black !important;">{{cya.countryname}}</option>
                                  </select>
                                  <div class="icon is-small is-left">
                                    <i class="fas fa-globe" style="color: rgb(55,195,255)"></i>
                                  </div>
                              </div>
                            </div>
                            <!-- statepref errors-->
                            <div v-if="errors.statePrefErrors.length">
                              <p class="my-errors" style="color:red" v-for="error in errors.statePrefErrors" v-bind:key="error">
                              <span style="color:red !important">*</span> {{ error }}
                              </p>                        
                            </div>
                            <!-- prefectures -->
                            <div v-if="this.country === 'JP'" class="field">
                              <label class="my-label has-text-black">{{$t('paymentmodal.pref')}}</label>
                              <div class="control">
                                <select v-model="statePref" name="statepref" class="input">
                                  <option value="" disabled selected hidden>
                                          {{$t('paymentmodal.prefplaceholder')}}
                                  </option>
                                  <option v-for="pref in $store.state.prefectures" :key="pref.prefval" :value="pref.prefval" style="color: black !important;">{{pref.prefval}}</option>
                                </select>
                              </div>
                            </div>
                            <!-- states -->
                            <div v-if="this.country === 'US'" class="field">
                              <label class="my-label has-text-black">{{$t('paymentmodal.state')}}</label>
                              <div class="control">
                                <select v-model="statePref" name="statepref" class="input">
                                  <option value="" disabled selected hidden>
                                          {{$t('paymentmodal.stateplaceholder')}}
                                  </option>
                                  <option v-for="state in $store.state.usstates" :key="state.stateval" :value="state.stateval" style="color: black !important;">{{state.statename}}</option>
                                </select>
                              </div>
                            </div>
                            <!-- post code errors-->
                            <div v-if="errors.zipcodeErrors.length">
                              <p class="my-errors" style="color:red" v-for="error in errors.zipcodeErrors" v-bind:key="error">
                              <span style="color:red !important">*</span> {{ error }}
                              </p>                        
                            </div>
                            <div class="field">
                              <label class="my-label has-text-black">{{$t('paymentmodal.postcode')}}</label>
                              <div class="control">
                                  <input type="text" class="input" :placeholder="$t('paymentmodal.postcodeplaceholder')" v-model="zipcode">
                              </div>
                            </div>
                        </div>
                      </div>
                    </div>
                    <hr>
                </div>
              </div>
              <!-- general errors -->
              <div v-if="errors.generalErrors.length">
                <p class="my-errors" style="text-align: center; color:red; padding-bottom: 1rem; padding-inline: 2.2rem;" v-for="error in errors.generalErrors" v-bind:key="error">
                  <span style="color:red !important">*</span> {{ error }}
                </p>                        
              </div>
              <div class="mb-5 has-text-black">
                <h2 class="my-credit-card-subtitle has-text-black">{{ $t('paymentmodal.cardinfo') }}</h2>
              </div>
              <div class="stripe-card-div">
                <div id="card-element" class="mb-5 control"></div>
              </div>
            </section>
            <!-- for usd -->
            <footer v-if="$store.state.region === 'US'" class="card-foot">
              <p class="my-subtotal has-text-black">
                <span>{{$t('cartview.total')}}:</span>
                <span style="padding-left: 0.5rem;" data-cart--cart-target="total">${{ usdPrice }}</span>
              </p>
              <p class="my-subtotal has-text-black">
                <span>{{$t('cartview.tax')}}:</span>
                <span style="padding-left: 0.5rem;" data-cart--cart-target="total">${{ calculateUsdTaxes }}</span>
              </p>
              <p class="my-subtotal has-text-black">
                <span>{{$t('cartview.subtotal')}}:</span>
                <span style="padding-left: 0.5rem;" data-cart--cart-target="total">${{ calculateUsdSubtotal }}</span>
              </p>
              <button @click.stop="submitForm();" :disabled="paymentProcessing" class="my-button-buy-now button">
                <span v-if="paymentProcessing">
                  {{$t('paymentmodal.paymentprocessing')}}
                </span>
                <span v-else>
                  {{$t('paymentmodal.pay')}} ${{ calculateUsdSubtotal }}
                </span>
              </button>
              <!-- if adding to cart, add the item to cart and close modal -->
              <button @click="show = false; clearFields(); checkoutClicked = false;" class="my-button-cancel button">
                {{$t('paymentmodal.cancel')}}
              </button>
            </footer>
            <!-- for jpy -->
            <footer v-else-if="$store.state.region === 'JP'" class="card-foot">
              <p class="my-subtotal has-text-black">
                <span>{{$t('cartview.total')}}:</span>
                <span style="padding-left: 0.5rem;" data-cart--cart-target="total">¥{{ jpyPrice }}</span>
              </p>
              <p class="my-subtotal has-text-black">
                <span>{{$t('cartview.tax')}}:</span>
                <span style="padding-left: 0.5rem;" data-cart--cart-target="total">¥{{ calculateJpyTaxes }}</span>
              </p>
              <p class="my-subtotal has-text-black">
                <span>{{$t('cartview.subtotal')}}:</span>
                <span style="padding-left: 0.5rem;" data-cart--cart-target="total">¥{{ calculateJpySubtotal }}</span>
              </p>
              <button @click.stop="submitForm();" :disabled="paymentProcessing" class="my-button-buy-now button">
                <span v-if="paymentProcessing">
                  {{$t('paymentmodal.paymentprocessing')}}
                </span>
                <span v-else>
                  {{$t('paymentmodal.pay')}} ¥{{ calculateJpySubtotal }}
                </span>
              </button>
              <!-- if adding to cart, add the item to cart and close modal -->
              <button @click="show = false; clearFields(); checkoutClicked = false;" class="my-button-cancel button">
                {{$t('paymentmodal.cancel')}}
              </button>
            </footer>
          </div>
    </div>
</template>


<!-- cart modal animation fade-in/out -->
<style>
  .v-enter-active,
  .v-leave-active {
    transition: opacity 0.3s ease;
  }

  .v-enter-from,
  .v-leave-to {
    opacity: 0;
  }
</style>


<script>
// @ is an alias to /src

// use axios to get api data from backend to frontend
// axios was installed during initial vue setup. found in package.json
// need to import axios in main.js as well
import axios from 'axios'
// for pop up notifying user about added item to cart
import { toast } from 'bulma-toast'
// import howler
import { Howl, Howler } from 'howler';
export default {
  name: 'Music',
  // data() is a new obj returning tracks list used in for loop above
  data() {
    return {
      paymentProcessing: false,
      purchaseButtonClicked: false,
      show: false,
      usdPrice: '',
      jpyPrice: '',
      usdTaxRate: .0,
      jpyTaxRate: 0.1,
      usdTax: '',
      jpyTax: '',
      usdSubTotal: '',
      jpySubtotal:'',
      modalOpened: false,
      tracks: [],
      setTrackID: '',
      setTrackTitle: '',
      isFree: '',
      // stripe stuff
      stripe: {},
      card: {},
      name: '',
      email: '',
      phone: '',
      address1: '',
      address2:'',
      statePref: '',
      country: '',
      zipcode: '',
      errors: {
              generalErrors: [],
              nameErrors: [],
              emailErrors: [],
              phoneErrors: [],
              address1Errors: [],
              address2Errors: [],
              statePrefErrors: [],
              countryErrors: [],
              zipcodeErrors: [],
          },      
      // check if this a USD or JPY payment
      isUsd: true,
    // number the tracks for UI/UX media player
    trackNumber: 0,
    lastPlayedTrack: 0,
    // to change slidebar color on hover
    slideBarHovering: false,
    // for repeat icon
    isRotated: false,
    // shuffle icon
    isInverted: false,
    }
  },

  components: {
  },
  // Vue lifecycle hook mounted() is called when this component is added to the DOM
  // so I guess on page load, getTracks() is called  
  mounted() {

    this.getTracks();
    document.addEventListener('click', this.closeModalOnWindowClick);
    this.$store.state.region === 'US' ? this.stripe = Stripe(process.env.VUE_APP_STRIPEPK, {locale: 'en'}) : this.stripe = Stripe(process.env.VUE_APP_STRIPEPK, {locale: 'ja'})
    const elements = this.stripe.elements();
    this.card = elements.create('card', { hidePostalCode: true })
    this.card.mount('#card-element')
    // set slidebar and slider in mount
    this.$store.state.slideBar = document.getElementById('slideBar'); 
    this.$store.state.slider = document.getElementById('slider'); 

  },

  computed: {

    calculateUsdTaxes() {
      var taxAmount = (parseFloat(this.usdTaxRate * this.usdPrice))
      this.usdTax = taxAmount.toFixed(2);
      return this.usdTax
    },
    calculateUsdSubtotal() {
      // prepending unary operator to these values to treat them as numbers
      // instead of strings for tax calc
      this.usdSubTotal = parseFloat(((this.usdPrice) + (+this.usdTax))).toFixed(2);
      return this.usdSubTotal;
    },

    calculateJpyTaxes() {
      var taxAmount = (parseFloat(this.jpyTaxRate * this.jpyPrice))
      this.jpyTax = taxAmount;
      return this.jpyTax
    },
    calculateJpySubtotal() {
      this.jpySubtotal = parseFloat((this.jpyPrice + this.jpyTax));
      return this.jpySubtotal
    },

  },

  // functions defined here
  methods: {

    // NEW MUSIC PLAYER IMPLEMENTATION
    // MOUSE SLIDEBAR CONTROLS
    sliderMoveDesktop(event) {
      let isClicking = false;
      let clickTimeout = null;

      // need to set up variables that are used by both single touch and long press events
      let seekTime = ''
      this.$store.state.slideBar = event.currentTarget
      this.$store.state.slideBarRect = this.$store.state.slideBar.getBoundingClientRect()
      let x = event.clientX - this.$store.state.slideBarRect.left

      const startDragDesktop = (event) => {
        isClicking = false;
        clickTimeout = setTimeout(() => {
          isClicking = true;
        }, 200);
        this.$store.state.isDragging = true;
        this.slideBarHovering = true
        this.$store.state.slider.classList.add('dragging');

      };

      const dragDesktop = (event) => {
        if (isClicking) {
          clearTimeout(clickTimeout);
          clickTimeout = null;
          event.preventDefault();

          this.$store.state.isDragging = true
          this.slideBarHovering = true
          // Add the 'dragging' class to the slider element
          this.$store.state.slider.classList.add('dragging');

          if (!this.$store.state.currentAudioElement || !this.$store.state.currentAudioElement.duration() || !this.$store.state.slideBarRect) {
            return;
          }
            this.$store.state.slideBar = this.$refs.slideBar
            this.$store.state.slideBarRect = this.$store.state.slideBar.getBoundingClientRect()
            let x = event.clientX - this.$store.state.slideBarRect.left
            const progress = Math.min(Math.max(x / this.$store.state.slideBarRect.width * 100, 0), 100)
            const duration = this.$store.state.currentAudioElement.duration()
            this.$store.commit('formatTime', (progress / 100) * duration)
            // this is used to update the seek playback position whenever the mouse is lifted
            seekTime = (this.$store.state.progress / 100) * duration

            this.$store.state.progress = progress
            this.updateSlideBarBackground()
          }
      };

      const endDragDesktop = (event) => {
        if (!isClicking) {

          this.$store.state.isDragging = false;
          this.slideBarHovering = false
          
          // Remove the 'dragging' class from the slider element
          this.$refs.slideBar.classList.remove('dragging');

          if (!this.$store.state.currentAudioElement || !this.$store.state.currentAudioElement.duration() || !this.$store.state.slideBarRect) {
            clearTimeout(clickTimeout);
            clickTimeout = null;
            document.removeEventListener('mousedown', startDragDesktop);
            document.removeEventListener('mousemove', dragDesktop);
            document.removeEventListener('mouseup', endDragDesktop);
            return;
          }


          this.$store.state.slideBar = this.$refs.slideBar
          const progress = Math.min(Math.max(x / this.$store.state.slideBarRect.width * 100, 0), 100)

          const duration = this.$store.state.currentAudioElement.duration()
          seekTime = (progress / 100) * duration

          this.$store.state.currentAudioElement.seek(seekTime)

          this.$store.commit('formatTime', seekTime)

          this.$store.state.progress = progress
          this.updateSlideBarBackground()
        }
        else {
          if (!this.$store.state.currentAudioElement) {
            return
          }
          this.$store.state.isDragging = false
          this.slideBarHovering = false
          
          // Remove the 'dragging' class from the slider element
          this.$refs.slideBar.classList.remove('dragging');

          this.$store.state.currentAudioElement.seek(seekTime)
        }
        clearTimeout(clickTimeout);
        clickTimeout = null;
        document.removeEventListener('mousedown', startDragDesktop);
        document.removeEventListener('mousemove', dragDesktop);
        document.removeEventListener('mouseup', endDragDesktop);
        
        this.slideBarHovering = false
        // Remove the 'dragging' class from the slider element
        this.$store.state.slider.classList.remove('dragging');
      };

      document.addEventListener('mousedown', startDragDesktop);
      document.addEventListener('mousemove', dragDesktop);
      document.addEventListener('mouseup', endDragDesktop);
    },

    // MOBILE SLIDEBAR CONTROLS
    // user touched slidebar, determine if it is a single tap or a long press
    sliderMoveMobile(event) {
      
      // prevent the screen from scrolling up and down
      // Check if scrolling is in progress
      if (event.cancelable && !event.defaultPrevented) {
        event.preventDefault();
      }      

      // need to set up variables that are used by both single touch and long press events
      let seekTime = ''
      this.$store.state.slideBar = event.currentTarget
      this.$store.state.slideBarRect = this.$store.state.slideBar.getBoundingClientRect()
      let x = event.touches[0].clientX - this.$store.state.slideBarRect.left
      let isTouching = true;


      let touchTimeout = setTimeout(() => {
        isTouching = false;
      }, 300);
      
      const clearTouchTimeout = () => {
        clearTimeout(touchTimeout);
        isTouching = false;
      };
      
      // for dragging slider
      const dragMobile = (event) => {
        clearTouchTimeout();
        this.$store.state.isDragging = true
        if (!this.$store.state.currentAudioElement || !this.$store.state.currentAudioElement.duration() || !this.$store.state.slideBarRect) {
          return;
        }
          this.$store.state.slideBar = this.$refs.slideBar
          this.$store.state.slideBarRect = this.$store.state.slideBar.getBoundingClientRect()
          let x = event.touches[0].clientX - this.$store.state.slideBarRect.left
          const progress = Math.min(Math.max(x / this.$store.state.slideBarRect.width * 100, 0), 100)
          const duration = this.$store.state.currentAudioElement.duration()
          this.$store.commit('formatTime', (progress / 100) * duration)
          seekTime = (this.$store.state.progress / 100) * duration

          this.$store.state.progress = progress
          this.updateSlideBarBackground()
      };

      // handles single tap and long press events
      const endDragMobile = (event) => {        
        // single taps
        if (isTouching) {
          clearTouchTimeout();
          this.$store.state.isDragging = false
          // don't move slider if a song hasn't been played yet (NEED TO FIX THIS LATER)
          if (!this.$store.state.currentAudioElement || !this.$store.state.currentAudioElement.duration() || !this.$store.state.slideBarRect) {
            return;
          }
          this.$store.state.slideBar = this.$refs.slideBar
          const progress = Math.min(Math.max(x / this.$store.state.slideBarRect.width * 100, 0), 100)

          const duration = this.$store.state.currentAudioElement.duration()
          seekTime = (progress / 100) * duration
          this.$store.state.currentAudioElement.seek(seekTime)

          this.$store.commit('formatTime', seekTime)
          // this.$store.state.songProgress = this.$store.state.minsecs

          this.$store.state.progress = progress
          this.updateSlideBarBackground()
        }
        // long press events. See const DragMobile
        else {
          this.$store.state.isDragging = false
          // set playtime based on seekTime var calculated in dragMobile
          this.$store.state.currentAudioElement.seek(seekTime)
        }
        // clear timeout and remove event listeners
        clearTouchTimeout();
      };
      
      event.target.addEventListener('touchmove', dragMobile, { passive: true });
      event.target.addEventListener('touchend', endDragMobile, { once: true });
    },

    // update slidebar color when slider moves along slidebar
    updateSlideBarBackground() {
      this.$store.state.slideBar = document.getElementById('slideBar'); 
      this.$store.commit('updateSlideBarBackground')
    },
    updateSliderDisplay() {
      this.$store.commit('updateSliderDisplay')
    },
      // timer to display track playback time
    formatTime(secs) {
      this.$store.commit('formatTime', secs)
    },

    // SLIDE BAR called by howl
    animateSlider() {
      this.$store.commit('animateSlider')
    },

    // remove event listeners if they are still active
    beforeDestroy() {
      // stop the recursion when the component is destroyed
      this.$store.state.slideBar = this.$refs.slideBar
      this.$store.state.slideBar.removeEventListener("mousedown", this.touchStartMobile)
      document.removeEventListener("mousemove", this.dragHandler)
      document.removeEventListener("mouseup", this.endDrag)
    },

    // MUSIC CONTROLLERS
    // SKIP TO NEXT TRACK
    skipForwardController() {
      this.$store.commit('skipForwardController')
    },
    // SKIP TO PREVIOUS TRACK
    skipPreviousController() {
      this.$store.commit('skipPreviousController')
    },
    // FOR PLAY/PAUSE BUTTON CONTROLLERS
    playPauseController() {
      this.$store.commit('playPauseController')
    },
    // Individual PLAY/RESUME TRACK
    setPlayOrPause(trackId) {
      // can only send one param to vuex mutations
      this.$store.commit('setPlayOrPause', trackId)
    },
    // SHUFFLE PLAYLIST
    // populateShufflePlaylist() {
    //   this.$store.commit('populateShufflePlaylist')
    // },
    // TOGGLE SHUFFLE
    toggleShuffle() {
      this.isInverted = !this.isInverted;
      if (this.isInverted) {
        this.isRotated = false
      }
      this.$store.commit('toggleShuffle')
    },
    // TOGGLE REPEAT
    toggleRepeat() {
      this.isRotated = !this.isRotated;
      if (this.isRotated) {
        this.isInverted = false
      }
      this.$store.commit('toggleRepeat')
    },
    // redirect to login screen
    redirectToLogin() {

        this.$router.push({ path: '/login', query: { loginwarning: true }})
    },
    // scroll to top of payment form
    scrollToBottom() {
      // wait until modal closes, then scroll to payment form
      this.$nextTick(() => this.$refs["paymentFormTop"].scrollIntoView({ behavior: "smooth" }))
    },
    // BUY NOW METHODS
    submitForm() {
      this.paymentProcessing = true;
      this.errors.generalErrors = []
      this.errors.nameErrors = []
      this.errors.emailErrors = []
      this.errors.phoneErrors = []
      this.errors.address1Errors = []
      this.errors.address2Errors = []
      this.errors.statePrefErrors = []
      this.errors.countryErrors = []
      this.errors.zipcodeErrors = []

      if (this.name === '') {
          this.paymentProcessing = false;
          this.errors.nameErrors.push('The name field is missing!')
      }
      if (this.email === '') {
          this.paymentProcessing = false;
          this.errors.emailErrors.push('The email field is missing!')
      }
      if (this.phone === '') {
          this.paymentProcessing = false;
          this.errors.phoneErrors.push('The phone field is missing!')
      }
      if (this.address1 === '') {
          this.paymentProcessing = false;
          this.errors.address1Errors.push('The address field is missing!')
      }
      if (this.statePref === '') {
          this.paymentProcessing = false; 
          this.errors.statePrefErrors.push('The state field is missing!')
      }        
      if (this.country === '') {
          this.paymentProcessing = false;
          this.errors.countryErrors.push('The country field is missing!')
      }
      if (this.zipcode === '') {
          this.paymentProcessing = false;
          this.errors.zipcodeErrors.push('The zip code field is missing!')
      }

      // if there are no form validation errors, process payment
      if (
          !this.errors.nameErrors.length &&
          !this.errors.emailErrors.length &&
          !this.errors.phoneErrors.length &&
          !this.errors.address1Errors.length &&
          !this.errors.address2Errors.length &&
          !this.errors.statePrefErrors.length &&
          !this.errors.countryErrors.length &&
          !this.errors.zipcodeErrors.length &&
          !this.errors.generalErrors.length
        ) {
          // set loading animation icon
          this.$store.commit('setIsLoading', true)

          // create stripe token based on user card input
          this.stripe.createToken(this.card).then(result => {                    
              if (result.error) {
                  this.$store.commit('setIsLoading', false)
                  this.paymentProcessing = false
                  this.errors.generalErrors.push('Something went wrong with Stripe. Please try again')
                  console.log(result.error.message)
              } 
              // if there are no stripe processing errors
              else {
                  this.stripeTokenHandler(result.token)
              }
          })
        }
    },
    // single flp purchase
    async stripeTokenHandler(token) {

      // send empty flp items for backend
      const flp_items = []
      const flp_obj = {
            no_flps: ''
          }
      flp_items.push(flp_obj)

      const track_items = []
      const track_obj = {
        track: this.setTrackID,
        usd_track_price: this.usdPrice,        
        jpy_track_price: this.jpyPrice,
      }
      track_items.push(track_obj)


      var jpy_paid_amount = 0
      var usd_paid_amount = 0
      // set currency based on language which is being used to set the region as well
      this.$store.state.region === 'US' ? (usd_paid_amount = this.calculateUsdSubtotal, jpy_paid_amount = 0) : (usd_paid_amount = 0, jpy_paid_amount = this.calculateJpySubtotal)
      // get customer billing data as well as stripe token and all
      // cart items, both flps and tracks 
      const data = {
        'name': this.name,
        'email': this.email,
        'phone': this.phone,
        'address1': this.address1,
        'address2': this.address2,
        'statePref': this.statePref,
        'country': this.country,
        'zipcode': this.zipcode,
        'flp_items': flp_items,
        'track_items': track_items,
        'stripe_token': token.id,
        'jpy_paid_amount': jpy_paid_amount,
        'usd_paid_amount': usd_paid_amount,
      }
      // post data to server; have to send token as well
      await axios
      .post(process.env.VUE_APP_CHECKOUT_API_URL, data,  {headers: { 'Authorization': `Token ${this.$store.state.sf_auth_bearer}`}})
      .then(response => {
        // reset store
        this.$store.state.downloadableItems = []
        this.$store.state.downloadableItems = response.data        
        // redirect to thank you page
        this.paymentProcessing = false;
        this.$router.push('/thankyou')
      })
      .catch(error => {
        console.log(error)
        this.paymentProcessing = false;
        this.errors.generalErrors.push('Something went wrong. Please try again later')
      })

      this.$store.commit('setIsLoading', false)
    },

    showPaymentForm() {
      return this.show === true ? {display: 'block'} : {display: 'none'}
    },
    clearFields() {
      this.name = ''
      this.email = ''
      this.phone = ''
      this.address1 = ''
      this.address2 = ''
      this.zipcode = ''
      this.statePref = '',
      this.country = '',
      this.errors.generalErrors = []
      this.errors.nameErrors = []
      this.errors.emailErrors = []
      this.errors.phoneErrors = []
      this.errors.address1Errors = []
      this.errors.address2Errors = []
      this.errors.statePrefErrors = []
      this.errors.countryErrors = []
      this.errors.zipcodeErrors = []
    },

    // set flp name and id
    buyNow(){
      this.$store.state.isSingleTrackDownload = true;
      this.$store.state.downloadType = 'fromMusicView'; 
    },

    // download one free track now
    async downloadFreeNow(track, id) {
      // FOR FRONTEND TO PREPARE FOR DOWNLOADS
      this.$store.state.freeDownload = track;
      this.$store.state.freeDownloadId = id;
      this.$store.state.isSingleTrackDownload = true;
      this.$store.state.downloadType = 'fromMusicView'; 
      var index = this.tracks.findIndex(x => x.id === id);
      const track_obj = {
        track: this.tracks[index].track,
        title: this.tracks[index].title
      }
      this.$store.state.downloadableItems = []
      this.$store.state.downloadableItems.push(track_obj)

      // SEND DATA TO BACKEND
      const flp_items = []
      const flp_obj = {
            no_flps: ''
          }
      flp_items.push(flp_obj)

      const track_items = []
        const track_obj_for_backend = {
          track: this.setTrackID,
        }
          track_items.push(track_obj_for_backend)

      // get user billing data as well as stripe token and all
      // cart items, both flps and tracks
      const data = {
        'flp_items': flp_items,
        'track_items': track_items,
      }

      // post data to server; have to send token as well
      await axios
      .post(process.env.VUE_APP_FREEDOWNLOAD_API_URL, data,  {headers: { 'Authorization': `Token ${this.$store.state.sf_auth_bearer}`}})
      .then(response => {
          // redirect to thank you page
          this.paymentProcessing = false;
          this.$router.push('/thankyou')
      })
      .catch(error => {
        console.log(error)
        this.paymentProcessing = false;
        this.errors.generalErrors.push('Something went wrong. Please try again later')
      })
      this.$store.commit('setIsLoading', false)

    },

    setTrack(track) {
      // set track name as well to show in modal popup
      const item = this.tracks.find(item => item.id === track)
      this.setTrackTitle = item.title;
      this.isFree = item.is_free;
      this.setTrackID = track;
      this.usdPrice = item.usd_price;
      this.jpyPrice = item.jpy_price;
    },

    closeModalOnWindowClick() {
      if (this.modalOpened === false) {

      }
      else if (this.modalOpened === true) {
        this.modalOpened = false;

      }
    },
    // number the tracks for UI/UX media player
    increment() {
      this.trackNumber++;
    },

    // make this method async and axios.get to await to make sure setIsLoading isn't set to false
    // until axios finished fetching api data
    async getTracks() {
      
      // loading bar while api data is getting fetched
      this.$store.commit('setIsLoading', true);
      // replace the API path with env var
      // .get requests API data from server via HTTP GET
      // .then will take the response data and populate the empty tracks list above
      await axios.get(process.env.VUE_APP_TRACKS_API_URL)
        .then(response => {
          this.tracks = response.data
          // set the tab title
          document.title = 'Music'
        })
        .catch(error => {
          console.log("ERROR BOYY: " + error)
        })

      // stop loading bar after api data is fetched
      this.$store.commit('setIsLoading', false);
    },

    // add to cart
    addTrackToCart(addTrackIdToCart) {

      // get specific track added to cart
      const item = this.tracks.find(item => item.id === addTrackIdToCart)

      // calls store/index.js addToCart function
      this.$store.commit('addToCart', item)

      // show toast msg to user https://www.npmjs.com/package/bulma-toast
      // toast fadein/out animation requires animate.css. See README
      toast({
        message: item.title + ' ' + this.$t('modals.addedtocart'),
        type: 'is-info',
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: 'bottom-right',
        animate: { in: 'fadeIn', out: 'fadeOut' },
      })
    },
    // remove from cart
    removeFromCart(removeItemID) {
      // get specific track added to cart
      const item = this.tracks.find(item => item.id === removeItemID)
      // pass entire json track/flp obj to removeFromCart function
      this.$store.commit('removeFromCart', item)
      toast({
        message: item.title + ' ' + this.$t('modals.removedfromcart'),
        type: 'is-danger',
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: 'bottom-right',
        animate: { in: 'fadeIn', out: 'fadeOut' },
      })
    },
    // check if an item clicked is already in the cart
    checkIfTrackIsInCart(track) {
      const pendingTrackCartItem = 
      this.
      $store.
      state.
      cart.
      itemsInCart.
      filter(i => i.title === track.title)
        if (pendingTrackCartItem.length) {
          return true;
        }
    }
  }
}
</script>