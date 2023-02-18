<template>
  <CCarousel controls indicators>
    <CCarouselItem>
      <img class="d-block w-100" :src="slides[0].image" alt="0" />
      <CCarouselCaption class="d-none d-md-block">
        <div>
          <h1 class="black_box">{{ slides[0].title }}</h1>
        </div>
        <p class="black_box">{{ slides[0].body }}</p>
      </CCarouselCaption>
    </CCarouselItem>
    <CCarouselItem>
      <img class="d-block w-100" :src="slides[1].image" alt="1" />
      <CCarouselCaption class="d-none d-md-block">
        <div>
          <h1 class="black_box">{{ slides[1].title }}</h1>
        </div>
        <p class="black_box">{{ slides[1].body }}</p>
      </CCarouselCaption>
    </CCarouselItem>
    <CCarouselItem>
      <img class="d-block w-100" :src="slides[2].image" alt="2" />
      <CCarouselCaption class="d-none d-md-block">
        <div>
          <h1 class="black_box">{{ slides[2].title }}</h1>
        </div>
        <p class="black_box">{{ slides[2].body }}</p>
      </CCarouselCaption>
    </CCarouselItem>
    <CCarouselItem>
      <img class="d-block w-100" :src="slides[3].image" alt="3" />
      <CCarouselCaption class="d-none d-md-block">
        <div>
          <h1 class="black_box">{{ slides[3].title }}</h1>
        </div>
        <p class="black_box">{{ slides[3].body }}</p>
      </CCarouselCaption>
    </CCarouselItem>
  </CCarousel>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { CCarousel, CCarouselItem, CCarouselCaption } from '@coreui/vue'
import '@coreui/coreui/dist/css/coreui.min.css'

export default defineComponent({
  name: 'Autoplay',
  components: {
    CCarousel,
    CCarouselItem,
    CCarouselCaption,
  },
  data() {
    return {
      slides: [
        {
          image: 'carousel/gimnasia_artistica.png',
          title: 'Gimnasia artística',
          body: 'de 8 a 14 años',
        },
        {
          image: 'carousel/handball.png',
          title: 'Handball',
          body: 'de 12 a 15 años',
        },
        {
          image: 'carousel/patin_artistico.png',
          title: 'Patín artístico',
          body: 'de 8 a 14 años',
        },
        {
          image: 'carousel/taekwon-do.png',
          title: 'Taekwon-do',
          body: 'de 12 a 18 años',
        },
      ],
    }
  },
})
</script>

<style scoped>
.own_holder {
  border: 2px;
  border-style: solid;
  border-color: #ad954b;
}

.black_box {
  background: rgba(0, 0, 0, 0.55);
  display: inline-block;
  padding-left: 1rem;
  padding-right: 1rem;
}

.short {
  width: 30rem;
}
</style>
