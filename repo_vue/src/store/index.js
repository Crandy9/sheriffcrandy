import { createStore } from 'vuex'
// import howler
import { Howl, Howler } from 'howler';

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


    // MUSIC PLAYER STATES
    // howl instance
    howlInstance: null,
     // add a new state property to store the seek time
    seekTime: 0,
    // the current track's html audio element playing
    currentAudioElement: null,
    // id of the current track playing
    currentAudioElementPlaying: null,
    // get the current img
    currentTrackImg: null,
    // used as a determiner for dragging the slider
    isDragging: false,
    // smooth slider animation
    animationFrame: null,
    // should hold the song's length in minute:seconds 00:00
    songLength: '- -',
    songProgress: '0:00',
    // percentage used to animate the slider along the slide bar
    progress: 0,
    // holds duration in 
    // duration: 51000,
    // the audio source of the track used by Howler.js
    currentSrc: '',
    // slidebar music view
    slideBar: '',
    // needed to prevent errors when slider is clicked before song starts playing
    slideBarRect: null,
    // used to persist the slidebar color
    slideBarBackground: '',
    isSlidebarHovering: false,
    // used to hide show the slider
    slider: null,
    // timer that updates the songprogress every second
    songTimer: '',
    // repeat song
    repeat: false,
    // shuffle flag
    shuffle: false,
    // array to hold ids of chosen shuffled tracks to not play duplicates
    shuffleArray: [],
    // last track of shuffle array
    shuffleArray_last_track: null,
    // playlist array needed by howlerjs
    // last track of playlist
    playlist_last_track: null,
    playlist: [],
    // currentTrackPlaying brought in state to persist
    currentTrackPlaying: null,
    // for songProgress
    minutes: '',
    seconds: '',
    // shuffle repeat states
    // repeat icon
    isRotated: false,
    isInverted: false,
    showMainMusicPlayer: false,
    // list of paid tracks
    purchasedTracksList: [],
    startTime: null

  },
  getters: {
    getLanguage: (state) => state.language
  },
  // synchronous functions; change states
  mutations: {

    // populate purchased tracks array
    populatePurchasedTrackArray(state, purchasedTracksList) {

      state.purchasedTracksList = purchasedTracksList
    },
    // remove all data from purchasedarray onlogout
    clearPurchasedTrackList(state) {

      state.purchasedTracksList = [];
    },

    // MUSIC FUNCTIONS:
    // update slidebar color
    updateSlideBarBackground(state, currentSlideBar) {

      // set the slidebar as either mini persist, persist, or music view player
      state.slideBar = currentSlideBar

      if (!state.slideBar) {
        return;
      }


      const defaultColor = '#00EEFF'
      const progress = state.progress;
      const isMobileScreen = window.innerWidth <= 1023;

      if (isMobileScreen) {
        const gradient = `linear-gradient(to right, ${defaultColor} ${progress}%, #ffffff ${progress}%)`;
        state.slideBar.style.background = gradient;
      } 
      
      else {
        const hoverColor = '#FFFF00'; // define the hover color
        const gradient = `linear-gradient(to right, ${defaultColor} ${progress}%, #ffffff ${progress}%)`;
        const hoverGradient = `linear-gradient(to right, ${hoverColor} ${progress}%, #ffffff ${progress}%)`;
        const background = state.isDragging || state.isSlidebarHovering ? hoverGradient : gradient;
        state.slideBar.style.background = background;
      }
    },
    
    // animate slider
    animateSlider(state) {
      // return if slider is animated without a song being set
      if (!state.currentAudioElement.duration()) {
        return;
      }
      const duration = state.currentAudioElement.duration() || 1
      if (!state.isDragging) {
          state.progress = ((state.currentAudioElement.seek() || 0) / duration) * 100
          this.commit('updateSlideBarBackground', state.slideBar)
      }
      state.animationFrame = requestAnimationFrame(() => {
        this.commit('animateSlider')
      })
    },

    // format playback time under slidebar
    formatTime(state, secs) {

      let minutes = Math.floor(secs / 60) % 60;
      let seconds = Math.floor(secs % 60);
      seconds = seconds.toString().length === 1 ? `0${seconds}` : seconds;
      state.songProgress = `${minutes}:${seconds}`

    },

    // howler instance
    createHowlInstance(state , src) {
      const newHowlInstance = new Howl({
            src: [src],
            onplay: () => {

              // Stop the timer
              clearInterval(state.songTimer);

              state.animationFrame = requestAnimationFrame(() => {
                this.commit('animateSlider')
              })        
              
              // Set a short delay before setting up the timer
              setTimeout(() => {
                state.songTimer = setInterval(() => {
                  // Update the song progress every second
                  let seekTime = state.currentAudioElement.seek();
                  this.commit('formatTime', seekTime);
                }, 1000);
              }, 50);

            },
            onpause: () => {
              // Stop the timer
              clearInterval(state.songTimer);
              cancelAnimationFrame(state.animationFrame)
            },
            onstop: () => {
              cancelAnimationFrame(state.animationFrame)
              // Stop the timer
              clearInterval(state.songTimer);
              state.songTimer = null;
              // Reset the song progress to 0:00
              state.songProgress = '0:00';
            },
            // when the song finishes playing go to next song
            onend: () => {

              let currentPlaylist = []
              let currentLastTrack = null

              if (state.shuffle) {
                currentPlaylist = state.shuffleArray
                currentLastTrack = state.shuffleArray_last_track
              }
              else {
                currentPlaylist = state.playlist
                currentLastTrack = state.playlist_last_track
              }

              if (state.repeat) {
                // repeat the same song
                state.currentAudioElement.play()
                return
              }
              // else the end of the playlist was reached. Go back to first track and standby
              else if (state.currentTrackPlaying == currentLastTrack) {

                state.currentTrackPlaying = currentPlaylist[0].id
                state.currentAudioElement.currentTime = 0;
                state.songProgress = '0:00'
                state.progress = 0
                this.commit('updateSlideBarBackground', state.slideBar)
                var getSrc = currentPlaylist.find((t) => t.id === state.currentTrackPlaying)

                // set currentSrc to be either a sample or the full length song
                // if this current source is a purchased track or free, show full song details
                if(state.purchasedTracksList.find((t) => t.id === getSrc.id) || getSrc.is_free) {
                  state.currentSrc = getSrc.get_track
                  state.songLength = getSrc.get_track_duration
                }
                else {
                  state.currentSrc = getSrc.get_sample;
                  // set song length to sample rate
                  state.songLength = '0:49'
                }

                // howl instance
                this.commit('createHowlInstance', state.currentSrc)
                const newAudioElement = state.howlInstance

                state.currentAudioElement = newAudioElement 
                state.currentAudioElementPlaying = false;               
                state.currentAudioElement.stop()
              }
              // else play the next song in the playlist
              else {
                state.songTimer = setInterval(() => {
                  this.commit('skipForwardController')
                }, 400);
                // set a little delay before playing next song in playlist
              }
            },
            onloaderror: (error) => {
              console.log('error loading audio file', error)
            },
            onplayerror: (error) => {
              console.log('error playing audio file', error)
            },
      }); 
      state.howlInstance = newHowlInstance 
    },

    // MUSIC CONTROLLERS
    // PLAY/PAUSE CONTROLLERS
    playPauseController(state) {

      let currentPlayList = []
      state.shuffle === true ? currentPlayList = state.shuffleArray : currentPlayList = state.playlist

      // if song is null, play the first song in the state.playlist
      if (!state.currentAudioElement) {

        var getSrc = currentPlayList.find((t) => t.id === currentPlayList[0].id)

        // set currentSrc to be either a sample or the full length song
        // check if this song was purchased by user
        if (state.purchasedTracksList.find((t) => t.id === getSrc.id) || getSrc.is_free) {
          state.currentSrc = getSrc.get_track
          state.songLength = getSrc.get_track_duration
        }
        else {
          state.currentSrc = getSrc.get_sample;
          // set song length to sample rate
          state.songLength = '0:49'
        }

        // howl instance
        this.commit('createHowlInstance', state.currentSrc)
        const newAudioElement = state.howlInstance

        state.currentAudioElement = newAudioElement
        state.currentAudioElement.play();
        state.currentAudioElementPlaying = true;
        this.commit('formatTime', state.currentAudioElement.seek())
        state.currentTrackPlaying = currentPlayList[0].id

      }
      // THIS WORKS else play/resume current song
      else if (state.currentAudioElementPlaying === false) {
        state.currentAudioElementPlaying = true;
        state.currentAudioElement.play();
      }
      // pause song
      else {
        state.currentAudioElementPlaying = false;
        state.currentAudioElement.pause();
      }
    },

    // Individual PLAY/RESUME TRACK
    setPlayOrPause(state, currentTrackId) {

      let currentPlayList = []
      const trackId = currentTrackId
      // const track_playlist = payload.track_playlist

      state.shuffle === true ? currentPlayList = state.shuffleArray : currentPlayList = state.playlist
      var getSrc = currentPlayList.find((t) => t.id === trackId)

      // set currentSrc to be either a sample or the full length song
      // if this current source is a purchased track or free, show full song details
      if (state.purchasedTracksList.find((t) => t.id === getSrc.id) || getSrc.is_free) {
        state.currentSrc = getSrc.get_track
        state.songLength = getSrc.get_track_duration
      }
      else {
        state.currentSrc = getSrc.get_sample;
        // set song length to sample rate
        state.songLength = '0:49'
      }

      // howl instance
      this.commit('createHowlInstance', state.currentSrc)
      const newAudioElement = state.howlInstance

      // THIS WORKS if no song has played yet, play the first one the user clicked 
      if (!state.currentAudioElement) {
        state.currentAudioElement = newAudioElement
        state.currentAudioElement.play()
        state.currentAudioElementPlaying = true
        state.currentTrackPlaying = trackId
      } 
      
      // THIS WORKS this is not the first song played
      else {
        // THIS WORKS play/pause/resume same song
        if (state.currentTrackPlaying == trackId) {
          // pause it
          if (state.currentAudioElement.playing()) {
            state.currentAudioElement.pause()
            state.currentAudioElementPlaying = false
            state.currentTrackPlaying = trackId
            this.commit('updateSlideBarBackground', state.slideBar)
            return
          } 
          // play it
          else {
            state.currentAudioElement.play()
            state.currentAudioElementPlaying = true
          }
        }
        // THIS WORKS this is a different song was chosen. Stop current song, set new song, and play it
        else {
          state.currentTrackPlaying = trackId
          state.currentAudioElement.stop()
          state.currentAudioElement = newAudioElement
          state.currentAudioElement.play()
          state.currentAudioElementPlaying = true
        }
      }
    },

    // SKIP FORWARD CONTROLLER
    skipForwardController(state) {

      state.songProgress = '0:00'

      // set the currentPlayList as either shuffle or normal
      let currentPlayList = []
      let currentLastTrack = null

      state.shuffle === true ? (currentPlayList = state.shuffleArray, currentLastTrack = state.shuffleArray_last_track) : (currentPlayList = state.playlist, currentLastTrack = state.playlist_last_track)

      // if no songs have been played, play first track
      if (!state.currentAudioElement) {
        state.currentTrackPlaying = currentPlayList[0].id

        var getSrc = currentPlayList.find((t) => t.id === state.currentTrackPlaying)

        // set currentSrc to be either a sample or the full length song
        // if this current source is a purchased track or free, show full song details
        if (state.purchasedTracksList.find((t) => t.id === getSrc.id) || getSrc.is_free) {
          state.currentSrc = getSrc.get_track
          state.songLength = getSrc.get_track_duration
        }
        else {
          state.currentSrc = getSrc.get_sample;
          // set song length to sample rate
          state.songLength = '0:49'
        }

        // set new audio element
        this.commit('createHowlInstance', state.currentSrc)
        const newAudioElement = state.howlInstance
  
        state.currentAudioElement = newAudioElement
        state.currentAudioElementPlaying = false
        state.songProgress = '0:00'
        state.currentAudioElement.stop()
      }
      // else if this is the last track in the currentPlayList, play the first track
      else if (state.currentTrackPlaying == currentLastTrack) {

        state.currentTrackPlaying = currentPlayList[0].id
        state.currentAudioElement.currentTime = 0;
        state.currentAudioElement.pause();        

        var getSrc = currentPlayList.find((t) => t.id === state.currentTrackPlaying)

        // set currentSrc to be either a sample or the full length song
        // if this current source is a purchased track or free, show full song details
        if (state.purchasedTracksList.find((t) => t.id === getSrc.id) || getSrc.is_free) {
          state.currentSrc = getSrc.get_track
          state.songLength = getSrc.get_track_duration
        }
        else {
          state.currentSrc = getSrc.get_sample;
          // set song length to sample rate
          state.songLength = '0:49'
        }

        // howl instance
        this.commit('createHowlInstance', state.currentSrc)
        const newAudioElement = state.howlInstance
              
        state.currentAudioElement = newAudioElement

        // if the song was playing, then play, else reset song and pause
        if (state.currentAudioElementPlaying === true) {
          state.currentAudioElement.play()
        }
        else {
          state.songProgress = '0:00'
          state.progress = 0
          this.commit('updateSlideBarBackground', state.slideBar)
          state.currentAudioElement.pause()
          state.currentAudioElementPlaying = false;
        }
      }

      // if the currently playing song is not the last track
      else {
        // local var containing the current track id needed for function below 
        var val = state.currentTrackPlaying
        // get the JSON object index of the current song in the currentPlayList
        var index = currentPlayList.findIndex(function(item){
          return item.id === val;
        });

        // get the id of the next track in the currentPlayList
        state.currentTrackPlaying = currentPlayList[index + 1].id
        state.currentAudioElement.currentTime = 0;
        state.currentAudioElement.pause();        

        var getSrc = currentPlayList.find((t) => t.id === state.currentTrackPlaying)

        // set currentSrc to be either a sample or the full length song
        // if this current source is a purchased track or free, show full song details
        if (state.purchasedTracksList.find((t) => t.id === getSrc.id) || getSrc.is_free) {
          state.currentSrc = getSrc.get_track
          state.songLength = getSrc.get_track_duration
        }
        else {
          state.currentSrc = getSrc.get_sample;
          // set song length to sample rate
          state.songLength = '0:49'
        }

        // howl instance
        this.commit('createHowlInstance', state.currentSrc)
        const newAudioElement = state.howlInstance

        state.currentAudioElement = newAudioElement
        // if the song was playing, then play, else reset song and pause
        if (state.currentAudioElementPlaying === true) {
          state.currentAudioElement.play()
        }
        else {
          state.songProgress = '0:00'
          state.progress = 0
          this.commit('updateSlideBarBackground', state.slideBar)
          state.currentAudioElement.pause()
          state.currentAudioElementPlaying = false;
        }        
      }
    },

    // SKIP PREVIOUS CONTROLLER
    skipPreviousController(state) {

      // set the currentPlayList as either shuffle or normal
      let currentPlayList = []
      let currentLastTrack = null

      state.shuffle === true ? (currentPlayList = state.shuffleArray, currentLastTrack = state.shuffleArray_last_track) : (currentPlayList = state.playlist, currentLastTrack = state.playlist_last_track)

      // get seconds from playback
      const [minutes, seconds] = state.songProgress.split(":");
      const secondsInt = parseFloat(seconds)

      // if progress is 1.5 seconds or more, replay song
      if (secondsInt >= 1) {
        state.currentAudioElement.stop();  
        state.progress = 0;
        this.commit('updateSlideBarBackground', state.slideBar)
        state.currentAudioElement.currentTime = 0; 

        // if the song was playing, then play, else reset song and pause
        if (state.currentAudioElementPlaying === true) {
          state.currentAudioElement.play()
        }
        else {
          state.currentAudioElement.pause()
        }
        return
      }
      var first_track = currentPlayList[0].id
  

      // THIS WORKS if no songs have been played, play the last track in the currentPlayList
      if (!state.currentAudioElement) {
        var getSrc = currentPlayList.find((t) => t.id === currentLastTrack)

        // set currentSrc to be either a sample or the full length song
        // if this current source is a purchased track or free, show full song details
        if (state.purchasedTracksList.find((t) => t.id === getSrc.id) || getSrc.is_free) {
          state.currentSrc = getSrc.get_track
          state.songLength = getSrc.get_track_duration
        }
        else {
          state.currentSrc = getSrc.get_sample;
          // set song length to sample rate
          state.songLength = '0:49'
        }

        // howl instance
        this.commit('createHowlInstance', state.currentSrc)
        const newAudioElement = state.howlInstance     

        state.currentAudioElement = newAudioElement;
        // if the song was playing, then play, else reset song and pause
        if (state.currentAudioElementPlaying === true) {
          state.currentAudioElement.play()
        }
        else {
          state.currentAudioElement.pause()
          state.currentAudioElementPlaying = false;
        }   

        state.currentTrackPlaying = currentLastTrack
      }

      // THIS WORKS skip back to the previous track
      else {
        // THIS WORKS if the current track playing is the first_track, play the last track
        if (state.currentTrackPlaying == first_track) {
          state.currentAudioElement.currentTime = 0;
          state.currentAudioElement.pause();        

          var getSrc = currentPlayList.find((t) => t.id === currentLastTrack)

          // set currentSrc to be either a sample or the full length song
          // if this current source is a purchased track or free, show full song details
          if (state.purchasedTracksList.find((t) => t.id === getSrc.id) || getSrc.is_free) {
            state.currentSrc = getSrc.get_track
            state.songLength = getSrc.get_track_duration
          }
          else {
            state.currentSrc = getSrc.get_sample;
            // set song length to sample rate
            state.songLength = '0:49'
          }

          // howl instance
          this.commit('createHowlInstance', state.currentSrc)
          const newAudioElement = state.howlInstance  

          state.currentAudioElement = newAudioElement
          // if the song was playing, then play, else reset song and pause
          if (state.currentAudioElementPlaying === true) {
            state.currentAudioElement.play()
          }
          else {
            state.currentAudioElement.pause()
            state.currentAudioElementPlaying = false;
          }   
          state.currentTrackPlaying = currentLastTrack
        }

        // THIS WORKS current track is not the first track
        else {
          state.currentAudioElement.currentTime = 0;
          state.currentAudioElement.pause();        

          var val = state.currentTrackPlaying
          var index = currentPlayList.findIndex(function(item){
            return item.id === val;
          });
          state.currentTrackPlaying = currentPlayList[index - 1].id

          var getSrc = currentPlayList.find((t) => t.id === state.currentTrackPlaying)

          // set currentSrc to be either a sample or the full length song
          // if this current source is a purchased track or free, show full song details
          if (state.purchasedTracksList.find((t) => t.id === getSrc.id) || getSrc.is_free) {
            state.currentSrc = getSrc.get_track
            state.songLength = getSrc.get_track_duration
          }
          else {
            state.currentSrc = getSrc.get_sample;
            // set song length to sample rate
            state.songLength = '0:49'
          }

          // howl instance
          this.commit('createHowlInstance', state.currentSrc)
          const newAudioElement = state.howlInstance  

          state.currentAudioElement = newAudioElement;
          if (state.currentAudioElementPlaying === true) {
            state.currentAudioElement.play()
          }
          else {
            state.currentAudioElement.pause()
            state.currentAudioElementPlaying = false;
          }  
        }
      }
    },

    // END CONTROLLERS

    // POPULATE PLAYLIST
    populatePlaylist(state, tracksList) {
      if (state.playlist.length) {
        return;
      }

      state.playlist = tracksList.slice(); // Make a copy of the array
      if (state.shuffle == false) {
        state.playlist_last_track = state.playlist[state.playlist.length - 1].id
      }
    },
    // POPULATE SHUFFLE Playlist
    populateShufflePlaylist(state) {

      // check if no song has played yet, and the user is spamming the shuffle button
      if (!state.currentTrackPlaying && state.shuffleArray.length !== 0) {
        return
      }


      // if there is already a shuffled playlist created
      // and the currently playing track is at the 0th index, 
      // that means the user turned the shuffle button on and off. Don't create a new playlist
      if (state.shuffleArray.length !== 0 && state.shuffleArray[0].id === state.currentTrackPlaying) {
        return
      }

      const shuffledArray = [];
      const originalArray = state.playlist.slice();
      

      for (let i = 0; i < originalArray.length; i++) {
        const randomIndex = Math.floor(Math.random() * (i + 1));
        if (randomIndex !== i) {
          shuffledArray[i] = shuffledArray[randomIndex];
        }
        shuffledArray[randomIndex] = originalArray[i];
      }

      // if there was a song currently playing when the shuffle button
      // was turned on, find the currently playing song's position in the shuffled array,
      // and swap it's position with the 0th index of the shuffled array

      if (state.currentTrackPlaying) {
        const currentTrackIndex = shuffledArray.findIndex(track => track.id === state.currentTrackPlaying);

        // if the currently playing song is already the first element by chance, good to go
        if (shuffledArray[currentTrackIndex] == shuffledArray[0]) {
          return
        }

        // else swap it with the current 0th element
        else {
          let placeholder = shuffledArray[0]
          shuffledArray[0] = shuffledArray[currentTrackIndex]
          shuffledArray[currentTrackIndex] = placeholder
        }


      }

      // set the state
      state.shuffleArray = shuffledArray;
      state.shuffleArray_last_track = shuffledArray[shuffledArray.length - 1].id;
    
    },

    // SHUFFLE CONTROLLER
    toggleShuffle(state) {

      state.isInverted = !state.isInverted;
      if (state.isInverted) {
        state.isRotated = false
      }
      // if repeat is true, set shuffle to false
      if (state.repeat && !state.shuffle) {
        state.repeat = false;
        state.shuffle = true;
      } 
      else {
        // otherwise toggle shuffle
        state.shuffle = !state.shuffle;
      }
      if (state.shuffle) {
        this.commit('populateShufflePlaylist')
      }
    },

    // REPEAT CONTROLLER
    toggleRepeat(state) {

      state.isRotated = !state.isRotated;
      if (state.isRotated) {
        state.isInverted = false
      }

      if (state.shuffle && !state.repeat) {
        // if shuffle is true, set repeat to false
        state.shuffle = false;
        state.repeat = true;
      } else {
        // otherwise toggle repeat
        state.repeat = !state.repeat;
      }
    },

    // called on app load/page refresh in App.vue entry point
    initializeStore(state) {

      // set locale and region
      // get the ip address
      // fetch('https://api.ipify.org?format=json')
      // .then(response => response.json())
      // .then(response => {
      //   state.clientIp = response.ip;
      // }).catch(error => console.log("GET IP API Error: " + error));
      
      // get data
    //  fetch('http://ip-api.com/json/' + state.clientIp + '?fields=status,message,country,countryCode')
    //   .then(response => response.json())
    //   .then(response => {
    //     // set initial region/language values based on IP address location
    //     if (state.initialLocaleSet == false) {
    //       if (response.country === 'Japan') {

    //       }
    //       else if (response.country === 'United States') {

    //       }
    //       // default
    //       else {

    //       }
    //       state.initialLocaleSet = true
    //     }
    //     else {
    //     }
    //   }).catch(error => console.log("GeoData API Error: " + error));


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
      localStorage.setItem("language", language)
    },
    // set region
    setRegion(state, region) {
      state.region = region;
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
