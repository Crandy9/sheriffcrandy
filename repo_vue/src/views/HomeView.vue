<template>
  <!-- homepage pic -->
  <section class="banner-section">
    <div class="home">
      <div class="scripture-banner">
        <h4 class="subtitle">
          “Blessed is the man that trusts in the Lord, and whose hope the Lord is."
        <p><cite>-Jeremiah 17:7 (KJV)</cite></p>
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
      <h2 class="is-size-2 has-text-centered has-text-white" id="yt-section-title">
        Latest Song
      </h2>
      <div class="yt-player">
        <iframe
          class="yt-iframe"
          src="https://www.youtube.com/embed/CNSDBPqTANo" 
          title="YouTube video player" 
          frameborder="0" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen>
        </iframe>
      </div>
  </section>
</template>