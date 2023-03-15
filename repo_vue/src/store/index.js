import { createStore } from 'vuex'

// cart implementation, authentication, etc.
// 
export default createStore({
  // state are vars that persist
  state: {

    // country dropdowns
    countries: [
      {countryname: "日本 (Japan)", countryval: "JP"},
      {countryname: "United States", countryval: "US"}
    ],
    // states
    usstates: [
      {statename: 'Armed Forces', stateval: 'Armed Forces - AA'},
      {statename: 'Armed Forces Europe', stateval: 'Armed Forces Europe - AE'},
      {statename: 'Armed Forces Pacific', stateval: 'Armed Forces Pacific - AP'},
      {statename: 'Alabama', stateval: 'Alabama'},
      {statename: 'Alaska', stateval: 'Alaska'},
      {statename: 'Arizona', stateval: 'Arizona'},
      {statename: 'Arkansas', stateval: 'Arkansas'},
      {statename: 'California', stateval: 'California'},
      {statename: 'Colorado', stateval: 'Colorado'},
      {statename: 'Connecticut', stateval: 'Connecticut'},
      {statename: 'Delaware', stateval: 'Delaware'},
      {statename: 'District of Columbia', stateval: 'District of Columbia'},
      {statename: 'Florida', stateval: 'Florida'},
      {statename: 'Georgia', stateval: 'Georgia'},
      {statename: 'Hawaii', stateval: 'Hawaii'},
      {statename: 'Idaho', stateval: 'Idaho'},
      {statename: 'Illinois', stateval: 'Illinois'},
      {statename: 'Indiana', stateval: 'Indiana'},
      {statename: 'Iowa', stateval: 'Iowa'},
      {statename: 'Kansas', stateval: 'Kansas'},
      {statename: 'Kentucky', stateval: 'Kentucky'},
      {statename: 'Louisiana', stateval: 'Louisiana'},
      {statename: 'Maine', stateval: 'Maine'},
      {statename: 'Maryland', stateval: 'Maryland'},
      {statename: 'Massachusetts', stateval: 'Massachusetts'},
      {statename: 'Michigan', stateval: 'Michigan'},
      {statename: 'Minnesota', stateval: 'Minnesota'},
      {statename: 'Mississippi', stateval: 'Mississippi'},
      {statename: 'Missouri', stateval: 'Missouri'},
      {statename: 'Montana', stateval: 'Montana'},
      {statename: 'Nebraska', stateval: 'Nebraska'},
      {statename: 'Nevada', stateval: 'Nevada'},
      {statename: 'New Hampshire', stateval: 'New Hampshire'},
      {statename: 'New Jersey', stateval: 'New Jersey'},
      {statename: 'New Mexico', stateval: 'New Mexico'},
      {statename: 'New York', stateval: 'New York'},
      {statename: 'North Carolina', stateval: 'North Carolina'},
      {statename: 'North Dakota', stateval: 'North Dakota'},
      {statename: 'Ohio', stateval: 'Ohio'},
      {statename: 'Oklahoma', stateval: 'Oklahoma'},
      {statename: 'Oregon', stateval: 'Oregon'},
      {statename: 'Pennsylvania', stateval: 'Pennsylvania'},
      {statename: 'Rhode Island', stateval: 'Rhode Island'},
      {statename: 'South Carolina', stateval: 'South Carolina'},
      {statename: 'South Dakota', stateval: 'South Dakota'},
      {statename: 'Tennessee', stateval: 'Tennessee'},
      {statename: 'Texas', stateval: 'Texas'},
      {statename: 'Utah', stateval: 'Utah'},
      {statename: 'Vermont', stateval: 'Vermont'},
      {statename: 'Virgin Islands', stateval: 'Virgin Islands'},
      {statename: 'Virginia', stateval: 'Virginia'},
      {statename: 'Washington', stateval: 'Washington'},
      {statename: 'West Virginia', stateval: 'West Virginia'},
      {statename: 'Wisconsin', stateval: 'Wisconsin'},
      {statename: 'Wyoming', stateval: 'Wyoming'},
      {statename: 'Guam', stateval: 'Guam'},
      {statename: 'Puerto Rico', stateval: 'Puerto Rico'},
    ],
    // prefectures
    prefectures: [
      // {prefname: "日本 (Japan)", prefval: "JP"}, 
      // {prefname: "United States", prefval: "US"}
      {prefname: 'Hokkaido',prefval:'北海道 Hokkaido'},
      {prefname: 'Aomori',prefval:'青森県 Aomori'},
      {prefname: 'Iwate',prefval:'岩手県 Iwate'},
      {prefname: 'Miyagi',prefval:'宮城県 Miyagi'},
      {prefname: 'Akita',prefval:'秋田県 Akita'},
      {prefname: 'Yamagata',prefval:'山形県 Yamagata'},
      {prefname: 'Fukushima',prefval:'福島県 Fukushima'},
      {prefname: 'Ibaraki',prefval:'茨城県 Ibaraki'},
      {prefname: 'Tochigi',prefval:'栃木県 Tochigi'},
      {prefname: 'Gunma',prefval:'群馬県 Gunma'},
      {prefname: 'Saitama',prefval:'埼玉県 Saitama'},
      {prefname: 'Chiba',prefval:'千葉県 Chiba'},
      {prefname: 'Tokyo',prefval:'東京都 Tokyo'},
      {prefname: 'Kanagawa',prefval:'神奈川県 Kanagawa'},
      {prefname: 'Niigata',prefval:'新潟県 Niigata'},
      {prefname: 'Toyama',prefval:'富山県 Toyama'},
      {prefname: 'Ishikawa',prefval:'石川県 Ishikawa'},
      {prefname: 'Fukui',prefval:'福井県 Fukui'},
      {prefname: 'Yamanashi',prefval:'山梨県 Yamanashi'},
      {prefname: 'Nagano',prefval:'長野県 Nagano'},
      {prefname: 'Gifu',prefval:'岐阜県 Gifu'},
      {prefname: 'Shizuoka',prefval:'静岡県 Shizuoka'},
      {prefname: 'Aichi',prefval:'愛知県 Aichi'},
      {prefname: 'Mie',prefval:'三重県 Mie'},
      {prefname: 'Shiga',prefval:'滋賀県 Shiga'},
      {prefname: 'Kyoto',prefval:'京都府 Kyoto'},
      {prefname: 'Osaka',prefval:'大阪府 Osaka'},
      {prefname: 'Hyogo',prefval:'兵庫県 Hyogo'},
      {prefname: 'Nara',prefval:'奈良県 Nara'},
      {prefname: 'Wakayama',prefval:'和歌山県 Wakayama'},
      {prefname: 'Tottori',prefval:'鳥取県 Tottori'},
      {prefname: 'Shimane',prefval:'島根県 Shimane'},
      {prefname: 'Okayama',prefval:'岡山県 Okayama'},
      {prefname: 'Hiroshima',prefval:'広島県 Hiroshima'},
      {prefname: 'Yamaguchi',prefval:'山口県 Yamaguchi'},
      {prefname: 'Tokushima',prefval:'徳島県 Tokushima'},
      {prefname: 'Kagawa',prefval:'香川県 Kagawa'},
      {prefname: 'Ehime',prefval:'愛媛県 Ehime'},
      {prefname: 'Kochi',prefval:'高知県 Kochi'},
      {prefname: 'Fukuoka',prefval:'福岡県 Fukuoka'},
      {prefname: 'Saga',prefval:'佐賀県 Saga'},
      {prefname: 'Nagasaki',prefval:'長崎県 Nagasaki'},
      {prefname: 'Kumamoto',prefval:'熊本県 Kumamoto'},
      {prefname: 'Oita',prefval:'大分県 Oita'},
      {prefname: 'Miyazaki',prefval:'宮崎県 Miyazaki'},
      {prefname: 'Kagoshima',prefval:'鹿児島県 Kagoshima'},
      {prefname: 'Okinawa',prefval: '沖縄県 Okinawa'}
    ],

    language: localStorage.getItem("language") || process.env.VUE_APP_I18N_LOCALE || 'en',
    region:  localStorage.getItem("region") || 'US',

    clientIp: '',
    langFromIpAPI: '',
    countryFromIpAPI: '',
    initialLocaleSet: false,

    downloadableItems: [],
    // web token used for authentication
    sf_auth_bearer: '',
    isAuthenticated: false,
    // set up cart state
    cart: {
        itemsInCart: [],
    },
    // show loading bar for cart
    isLoading: false,
    username: '',
    // free track/flp downloads
    isSingleTrackDownload: false,
    isSingleFlpDownload: false,
    isSingleCartDownload: false,
    isMultiFileDownload: false,
    freeDownload: '',
    freeDownloadId: '',
    downloadType: '',
  },
  getters: {
    getLanguage: (state) => state.language
  },
  // synchronous functions; change states
  mutations: {

    // called on app load/page refresh in App.vue entry point
    initializeStore(state) {

      // set locale and region
      // get the ip address
      fetch('https://api.ipify.org?format=json')
      .then(response => response.json())
      .then(response => {
        state.clientIp = response.ip;
        console.log('IP Address: ' + state.clientIp)
      }).catch(error => console.log("GET IP API Error: " + error));
      
      // get data
     fetch('http://ip-api.com/json/' + state.clientIp + '?fields=status,message,country,countryCode')
      .then(response => response.json())
      .then(response => {
        console.log('Response country: ' + response.country)
        // set initial region/language values based on IP address location
        if (state.initialLocaleSet == false) {
          console.log('setting locale and region for first time')
          if (response.country === 'Japan') {
            // state.region = 'JP';
            // state.language = 'ja';
            console.log(state.language)
            console.log(state.region)
          }
          else if (response.country === 'United States') {
            // state.region = 'US';
            // state.language = 'en';
            console.log(state.language)
            console.log(state.region)
          }
          // default
          else {
            // state.region = 'US';
            // state.language = 'en'
            console.log(state.language)
            console.log(state.region)
          }
          state.initialLocaleSet = true
        }
        else {
          console.log('Region manually set by user. Current location disregarded.')
        }
      }).catch(error => console.log("GeoData API Error: " + error));


      // check if user has a web token (logged in)
      if (localStorage.getItem('sf_auth_bearer')) {
        state.sf_auth_bearer = localStorage.getItem('sf_auth_bearer')
        state.isAuthenticated = true
      }
      else {
        state.sf_auth_bearer = ''
        state.isAuthenticated = false
      }
      // check if cart exists in local browser storage
      if (localStorage.getItem('cart')) {
          // get obj from storage if it exists
          state.cart = JSON.parse(localStorage.getItem('cart'))
      }
      // create empty cart in local browser storage
      else {
          localStorage.setItem('cart', JSON.stringify(state.cart))
      }
    },

    // set web token
    setToken(state, sf_auth_bearer) {
      state.sf_auth_bearer = sf_auth_bearer
      state.isAuthenticated = true
    },

    // remove token for logout
    removeToken(state) {
      state.sf_auth_bearer = ''
      state.isAuthenticated = false
    },

    // set language
    setLanguage(state, language) {
      state.language = language;
      console.log('language changed')
      console.log('new language:' + state.language)
      localStorage.setItem("language", language)
    },
    // set region
    setRegion(state, region) {
      state.region = region;
      console.log('region changed')
      console.log('new region:' + state.region)
      localStorage.setItem("region", region)
    },

    // add items to cart
    addToCart(state, item) {

      // check if this is an flp or track being added to cart
      var isTrack = false
      var is_flp = false

      if ('title' in item) {
        isTrack = true;
        is_flp = false;      
      }

      else if ('flp_name' in item) {
        isTrack = false;
        is_flp = true;   
      }


      // check if this track is already in the cart
      // will be either '[]' if not in cart.items, or '[proxy]'
      if (isTrack) {
        const pendingTrackCartItem = state.cart.itemsInCart.filter(i => i.title === item.title)
        // if track already exists
        // TODO: what to do if attempted duplicate cart item
        if (pendingTrackCartItem.length) {
        }
        // else if it doesn't exist push this track to the cart
        else {
              // push to cart
              state.cart.itemsInCart.push(item)
              // push to track array
              // state.trackItemsInCart.push(item)
        }

      }
      // check if this flp is already in the cart
      else if (is_flp) {
        const pendingFlpCartItem = state.cart.itemsInCart.filter(i => i.flp_name === item.flp_name)
        // TODO: what to do if attempted duplicate cart item
        if (pendingFlpCartItem.length) {
          }
        // else if it doesn't exist push this track/flp to the cart
        else {
              // push flp to cart
              state.cart.itemsInCart.push(item)
              // push flp to flp array
              // state.flpItemsInCart.push(item)
        }
      }

      // save cart storage data
      localStorage.setItem('cart', JSON.stringify(state.cart))
    },

    // remove items from cart
    removeFromCart(state, item) {
      // check if this is an flp or track being added to cart
      var isTrack = false
      var is_flp = false

      if ('title' in item) {
        isTrack = true;
        is_flp = false;      
      }

      else if ('flp_name' in item) {
        isTrack = false;
        is_flp = true;   
      }


      // make sure track is in cart
      if (isTrack) {
        // try to extract the object from the cart array
        const pendingTrackCartItemRemoval = state.cart.itemsInCart.filter(i => i.title === item.title)
        // if track exists
        if (pendingTrackCartItemRemoval.length) {

          // get track title used to find its location in the cart
          var track_title = pendingTrackCartItemRemoval[0].title
          // now using the track title, find the index of this track in the cart array
          var index = state.cart.itemsInCart.findIndex(x => x.title === track_title);

          // don't pop, but remove this specific track wherever it is located in the array
          state.cart.itemsInCart.splice(index, 1);
          // save cart storage data
          localStorage.setItem('cart', JSON.stringify(state.cart))
        }
        // else if it doesn't exist just return
        else {
          return
        }

      }
      // same with flps
      else if (is_flp) {
        // try to extract the object from the cart array
        const pendingFlpCartItemRemoval = state.cart.itemsInCart.filter(i => i.flp_name === item.flp_name)
        // if track exists
        if (pendingFlpCartItemRemoval.length) {

          // get track title used to find its location in the cart
          var flpName = pendingFlpCartItemRemoval[0].flp_name
          // now using the track title, find the index of this track in the cart array
          var index = state.cart.itemsInCart.findIndex(x => x.flp_name === flpName);

          // don't pop, but remove this specific track wherever it is located in the array
          state.cart.itemsInCart.splice(index, 1);
          // save cart storage data
          localStorage.setItem('cart', JSON.stringify(state.cart))
        }
        // else if it doesn't exist just return
        else {
          return
        }
      }
    },

    // remove all data from cart
    clearCart(state) {

      state.cart.itemsInCart = [];
      // update local storage
      localStorage.setItem('cart', JSON.stringify(state.cart))
    },

    // set a loading bar 
    setIsLoading(state, status) {
      state.isLoading = status;
    }
  },
  // asynchronous vars
  actions: {
  },
  modules: {
  }
})
