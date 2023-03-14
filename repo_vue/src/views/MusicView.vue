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
      <div v-for="trackDisplay in tracks" v-bind:key="trackDisplay.id">
        <!-- show img thumbnail for current track -->
        <!-- or leave title up after song stops playing -->
        <figure v-if="currentTrackPlaying == trackDisplay.id || (lastPlayedTrack == trackDisplay.id && stop == true)" class="track-img">
          <img class="cover-art" v-bind:src="trackDisplay.get_cover_art">
        </figure> 
        <h3 class="track-title-img" v-if="currentTrackPlaying == trackDisplay.id || (lastPlayedTrack == trackDisplay.id && stop == true)">
          Sheriff Crandy - {{ trackDisplay.title }}
        </h3>
      </div>
      <div>
        <h3 style="padding: 1rem;" v-if="currentTrackPlaying == 0" class="is-size-5 has-text-warning">
          {{$t('musicview.clicktohearsample')}}
        </h3>
      </div>
      <div class="skip-icons-wrapper">
        <div class="skip-icons">
          <span @click="prevTrack()">
            <i class="fa fa-fast-backward"></i>
          </span>
          <span @click="nextTrack()">
            <i class="fa fa-fast-forward"></i>  
          </span>
        </div>
      </div>
    </section>
    <section class="music-player-section">
      <!-- currently playing song -->
      <!-- unordered list of track -->
      <ul class="audio-player-ul">
        <!-- Vue for loop -->
        <div v-for="track, index in tracks" v-bind:key="track.id" class="media-player">
          <!-- play audio if play is true -->
          <audio class="hidden-player" controls autoplay v-if="play == true && pause == false && currentTrackPlaying == track.id">
            <source :src="track.get_sample" type="audio/mpeg">
            Your browser does not support the audio element.
          </audio>
          <div>
          </div>
          <li @click="setPlayOrPause(track.id)" class="track-list-item" v-bind:id="track.id">
            <!-- show play button on all tracks on hover -->
            <a class="play-button" href="#" v-if="currentTrackPlaying != track.id"> 
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
              v-if="(currentTrackPlaying == track.id && play == false && pause == true) || (lastPlayedTrack == track.id && play == false && pause == false && stop == true)">
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
            <a class="pause-button" href="#" v-if="currentTrackPlaying == track.id && play == true && pause == false">
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
            <span v-if="currentTrackPlaying != track.id" class="track-number">{{++index}}</span>
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
                <!-- open modal. click.stop prevents the parent click even from firing
                  doesn't play/pause the song, adds this item to cart only
                -->
                <a class="button is-small is-black price-button has-text-weight-medium" 
                  v-else-if="track.is_free" 
                  @click.stop="modalOpened = true; setTrack(track.id);" data-target="my-modal-id">
                  {{$t('cartview.free')}}

                </a>
                <a class="button is-small is-black price-button has-text-weight-medium" 
                  v-else-if="track.usd_price && $store.state.language === 'en'"
                  @click.stop="modalOpened = true; setTrack(track.id);" data-target="my-modal-id">
                  ${{ track.usd_price }}
                </a>
                <a class="button is-small is-black price-button has-text-weight-medium" 
                  v-else-if="track.usd_price && $store.state.language === 'ja'"
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
              <button v-if="isFree" @click="modalOpened = false; show = false; purchaseButtonClicked = false; downloadFreeNow(setTrackTitle, setTrackID);" class="my-modal-button-buy-now button">{{$t('cartview.downloadnow')}}</button>
              <!-- trigger stripe payment on this item only -->
              <button v-else @click="modalOpened = false; show = true; purchaseButtonClicked = true; buyNow(); scrollToBottom();" class="my-modal-button-buy-now button">{{$t('cartview.buynow')}}</button>
              <!-- if adding to cart, add the item to cart and close modal -->
              <button @click.stop="addTrackToCart(setTrackID); modalOpened = false" class="my-modal-button-add-to-cart button">{{$t('cartview.addtocart')}}</button>
            </footer>
          </div>
      </div>
    </Transition>
    <h2 class="music-guide is-size-5 has-text-centered has-text-warning">
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

  <transition>
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
            <footer v-if="$store.state.language === 'en'" class="card-foot">
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
              <button @click="submitForm();" class="my-button-buy-now button">{{$t('paymentmodal.pay')}} ${{ calculateUsdSubtotal }}</button>
              <!-- if adding to cart, add the item to cart and close modal -->
              <button @click="show = false; clearFields(); checkoutClicked = false;" class="my-button-cancel button">{{$t('paymentmodal.cancel')}}</button>
            </footer>
            <!-- for jpy -->
            <footer v-else-if="$store.state.language === 'ja'" class="card-foot">
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
              <button @click="submitForm();" class="my-button-buy-now button">{{$t('paymentmodal.pay')}} ¥{{ calculateJpySubtotal }}</button>
              <!-- if adding to cart, add the item to cart and close modal -->
              <button @click="show = false; clearFields(); checkoutClicked = false;" class="my-button-cancel button">{{$t('paymentmodal.cancel')}}</button>
            </footer>
          </div>
    </div>
  </transition>
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

export default {
  name: 'Music',
  // data() is a new obj returning tracks list used in for loop above
  data() {
    return {
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
      // track number
      trackNumber: 0,
      // player status
      play: false,
      pause: false,
      stop: true,
      currentTrackPlaying: 0,
      lastPlayedTrack: 0,
      currentTimer: '',
      currentSeconds: 0,
      currentInterval: '',
      // play sample for 51 seconds 
      duration: 51000,
      timeRemaining: 0,
    }
  },

  components: {
  },
  // Vue lifecycle hook mounted() is called when this component is added to the DOM
  // so I guess on page load, getTracks() is called  
  mounted() {
    this.getTracks();
    document.addEventListener('click', this.closeModalOnWindowClick);
    this.$i18n.locale === 'en' ? this.stripe = Stripe(process.env.VUE_APP_STRIPEPK, {locale: 'en'}) : this.stripe = Stripe(process.env.VUE_APP_STRIPEPK, {locale: 'ja'})
    const elements = this.stripe.elements();
    this.card = elements.create('card', { hidePostalCode: true })
    this.card.mount('#card-element')
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
    // scroll to top of payment form
    scrollToBottom() {
      console.log('scroll to payment form')
      // wait until modal closes, then scroll to payment form
      this.$nextTick(() => this.$refs["paymentFormTop"].scrollIntoView({ behavior: "smooth" }))
    },
    // BUY NOW METHODS
    submitForm() {
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
          this.errors.nameErrors.push('The name field is missing!')
      }
      if (this.email === '') {
          this.errors.emailErrors.push('The email field is missing!')
      }
      if (this.phone === '') {
          this.errors.phoneErrors.push('The phone field is missing!')
      }
      if (this.address1 === '') {
          this.errors.address1Errors.push('The address field is missing!')
      }
      if (this.statePref === '') {
          this.errors.statePrefErrors.push('The state field is missing!')
      }        
      if (this.country === '') {
          this.errors.countryErrors.push('The country field is missing!')
      }
      if (this.zipcode === '') {
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
      this.$store.state.language === 'en' ? (usd_paid_amount = this.calculateUsdSubtotal, jpy_paid_amount = 0) : (usd_paid_amount = 0, jpy_paid_amount = this.calculateJpySubtotal)
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
        this.$router.push('/thankyou')
      })
      .catch(error => {
        console.log(error)
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
          this.$router.push('/thankyou')
      })
      .catch(error => {
        console.log(error)
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

    // skip track forward
    nextTrack() {
      var last_track = this.tracks[this.tracks.length - 1].id
      // if no songs have been played, skip to second track in playlist 
      if (this.currentTrackPlaying == 0) {
        this.currentTrackPlaying = this.tracks[0].id
        this.play = true;
        this.stop = false;
        this.pause = false;
        clearTimeout(this.currentTimer)
        // start timer
        this.currentTimer = setTimeout(() => {
            this.stop = true; 
            this.lastPlayedTrack = this.currentTrackPlaying;
            this.play = false;
            this.pause = false;
          }, this.duration);
      }
      // else if this is the last track in the playlist, play the first track
      else if (this.currentTrackPlaying == last_track) {
        this.currentTrackPlaying = this.tracks[0].id
        this.play = true;
        this.stop = false;
        this.pause = false;
        clearTimeout(this.currentTimer)
        // start timer
        this.currentTimer = setTimeout(() => {
            this.stop = true; 
            this.lastPlayedTrack = this.currentTrackPlaying;
            this.play = false;
            this.pause = false;
          }, this.duration);
      }
      else {
        // local var containing the current track id needed for function below 
        var val = this.currentTrackPlaying
        // get the JSON object index of the current song in the playlist
        var index = this.tracks.findIndex(function(item){
          return item.id === val;
        });
        // get the id of the next track in the playlist
        this.currentTrackPlaying = this.tracks[index + 1].id

        this.play = true;
        this.stop = false;
        this.pause = false;
        clearTimeout(this.currentTimer)
        // start timer
        this.currentTimer = setTimeout(() => {
            this.stop = true; 
            this.lastPlayedTrack = this.currentTrackPlaying;
            this.play = false;
            this.pause = false;
          }, this.duration);
      }
    },
    prevTrack() {
      var first_track = this.tracks[0].id
      var last_track = this.tracks[this.tracks.length - 1].id

      // if no songs have been played or if current track is the first_track, play the last track in the playlist
      if (this.currentTrackPlaying == 0 || this.currentTrackPlaying == first_track) {
        this.currentTrackPlaying = last_track
        this.play = true;
        this.stop = false;
        this.pause = false;
        clearTimeout(this.currentTimer)
        // start timer
        this.currentTimer = setTimeout(() => {
            this.stop = true; 
            this.lastPlayedTrack = this.currentTrackPlaying;
            this.play = false;
            this.pause = false;
          }, this.duration);
      }
      // skip back to the previous track
      else {
        // same setup for nextTrack only reversed
        var val = this.currentTrackPlaying
        var index = this.tracks.findIndex(function(item){
          return item.id === val;
        });
        // get the id of the prev track in the playlist
        this.currentTrackPlaying = this.tracks[index - 1].id

        this.play = true;
        this.stop = false;
        this.pause = false;
        clearTimeout(this.currentTimer)
        // start timer
        this.currentTimer = setTimeout(() => {
            this.stop = true; 
            this.lastPlayedTrack = this.currentTrackPlaying;
            this.play = false;
            this.pause = false;
          }, this.duration);
      }

    },
    // number the tracks for UI/UX media player
    increment() {
      this.trackNumber++;
    },
    // for playing/pausing track
    setPlayOrPause(track) {

      // if currentTrackPlaying is 0, it means no song has been played
       if (this.currentTrackPlaying == 0 && this.play == false && this.pause == false && this.stop == true) {
        // set the current track to the track selected by user
        this.currentTrackPlaying = track
        this.play = true;
        this.stop = false;
        // start timer
        this.currentTimer = setTimeout(() => {
            this.stop = true; 
            this.lastPlayedTrack = this.currentTrackPlaying;
            this.play = false;
            this.pause = false;
          }, this.duration);        
      }
      // either pausing, resuming, or playing current track again
      else if (this.currentTrackPlaying == track) {
        // if the song is currently playing, pause it
        if (this.play == true && this.pause == false && this.stop == false) {
          this.pause = true;
          this.play = false;
          // get how many more seconds the song has to play
        }
        // if song is currently paused, resume it
        else if (this.play == false && this.pause == true && this.stop == false){
          this.pause = false;
          this.play = true;
          // 
          clearTimeout(this.currentTimer)
          // resume timeout
          // start new timer and set stop = true if full song plays
          this.currentTimer = setTimeout(() => {
            this.stop = true; 
            this.lastPlayedTrack = this.currentTrackPlaying;
            this.play = false;
            this.pause = false;
          }, this.duration); 
        }
        //  else if the song played all the way through and the user clicks it again, play it again
        else {
          this.pause = false;
          this.play = true;
          this.stop = false;
          clearTimeout(this.currentTimer)
          // resume timeout
          // start new timer and set stop = true if full song plays
          this.currentTimer = setTimeout(() => {
            this.stop = true; 
            this.lastPlayedTrack = this.currentTrackPlaying;
            this.play = false;
            this.pause = false;
          }, this.duration); 
        }
      }
      // stop current track and play new track
      else {
        // clear the timer that was playing
        clearTimeout(this.currentTimer)
        // set the new track
        this.currentTrackPlaying = track;
        this.play = true
        this.stop = false;
        this.pause = false;
        // start new timer
        this.currentTimer = setTimeout(() => {
            this.stop = true;
            this.lastPlayedTrack = this.currentTrackPlaying; 
            this.play = false;
            this.pause = false;
          }, this.duration);         
      }
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
          console.log(process.env.VUE_APP_TRACKS_API_URL)
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
        duration: 3000,
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
        duration: 3000,
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