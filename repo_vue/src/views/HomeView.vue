<template>
  <!-- homepage pic -->
  <section class="banner-section">
    <div class="home">
      <div class="scripture-banner">
        <h4 class="subtitle">
          "Make music to the Lord with the harp,
           with the harp and the sound of melody!
           With trumpets and the sound of the horn
           make a joyful noise before the King, the Lord!"
          <p style="font-size:medium"><cite>-Psalm 89:5-6 (esv)</cite></p>
        </h4>
      </div>
      <div class="has-text-centered">
        <figure>
          <img class="sheriff-crandy-img" src="@/assets/images/piano.jpg" alt="">
        </figure>
      </div>
    </div>
  </section>


  <!-- youtube video section -->
  <section class="latest-yt-songs-section">
      <h3 id="yt-section-title" class="is-size-3 has-text-centered has-text-white" >
        <u>Latest Songs/Covers</u>
      </h3>
      <div class="yt-player">
        <h3 id="yt-section-title" class="is-size-4 has-text-centered has-text-white" >
          "Simplicity"
        </h3>
        <iframe
          class="yt-iframe"
          src="https://www.youtube.com/embed/CNSDBPqTANo" 
          title="YouTube video player" 
          frameborder="0" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen>
        </iframe>
        <h3 id="yt-section-title" class="is-size-4 has-text-centered has-text-white" >
          "The Streets of Whiterun"
          <p class="is-size-5">[Sheriff Crandy cover]</p>
        </h3>
        <iframe
          class="yt-iframe"
          src="https://www.youtube.com/embed/UJkRxT4gb6A" 
          title="YouTube video player" 
          frameborder="0" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen>
        </iframe>
        <h3 class="is-size-4 has-text-white has-text-centered" style="padding-top: 3rem;">
          Purchase/download my songs<a class="music-links" href="/music"> here</a>!
        </h3>
      </div>
  </section>
</template>

<script>

export default {
    name: 'Home',
    data() {
      return {
        
      }
    },
    mounted() {
      document.title = 'Home' 
    },

}
</script>