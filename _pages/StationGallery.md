---
btn_label: Station Gallery
permalink: /StationGallery/
author_profile: false
layout: splash
entries_layout: grid
classes: wide
stations1:
  - image_path: /images/OK01.jpg
    alt: OK01-Olkaria1AU
    btn_label: "OK01 Olkaria 1AU"
    url: '/images/OK01.jpg'
  - image_path: /images/OK02.jpg
    alt: OK02-Geolab
    btn_label: OK02 KenGen Geolab
    url: '/images/OK02.jpg'
  - image_path: /images/OK04_question.jpg
    alt: OK03-OW914
    btn_label: "OK03 Well 914"
    url: '/images/OK04_question.jpg'
stations2:
  - image_path: /images/OK04.jpg
    alt: OK04-OW907
    btn_label: "OK04 Well 907"
    url: '/images/OK04.jpg'
  - image_path: /images/OK05.jpg
    alt: OK05-OW730
    btn_label: "OK05 Well 730"
    url: '/images/OK05.jpg'
  - image_path: /images/OK06.jpg
    btn_label: "OK06 Well 52"
    alt: OK06-OW52
    url: '/images/OK06.jpg'
stations3:
  - image_path: /images/OK07.jpg
    alt: OK07-KenGen-DinnerClub
    btn_label: "OK07 KenGen Dinner Club"
    url: '/images/OK07.jpg'
  - image_path: /images/OK08.jpg
    alt: OK08-Olomayiana
    btn_label: "OK08 Olomayiana"
    url: '/images/OK08.jpg'
  - image_path: /images/OK09.jpg
    alt: OK09-Naivasha
    btn_label: "OK09 Naivasha"
    url: '/images/OK09.jpg'
stations4:
  - image_path: /images/TUKN_3.jpg
    alt: TUKN-TechnicalUniversity
    btn_label: "TUKN Technical University of Kenya, Nairobi"
    url: '/images/TUKN_3.jpg'

---

<style>
  /* Station gallery only: crop every photo to the same 3:4 portrait box so all
     tiles are the same size and their captions/buttons line up. Scoped to
     .station-gallery so plot figures on the GNSS/Climate pages (same feature_row)
     are unaffected. */
  .station-gallery .archive__item-teaser { overflow: hidden; border-radius: 4px; }
  .station-gallery .archive__item-teaser img {
    display: block;
    width: 100%;
    aspect-ratio: 3 / 4;
    object-fit: cover;
    object-position: center;
  }
</style>

<div class="station-gallery">

{% include feature_row id="stations1" type=center%}

{% include feature_row id="stations2" type=center%}

{% include feature_row id="stations3" type=center%}

{% include feature_row id="stations4" type=center%}

</div>

