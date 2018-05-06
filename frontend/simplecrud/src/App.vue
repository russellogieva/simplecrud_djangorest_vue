<template lang="pug">
  #app
    div.container
      router-view
</template>

<script>

export default {
  name: 'App'
}
</script>

<style>
a, abbr, article, aside, audio, b, blockquote, body, cite, dd, del, div, dl, dt, em, fieldset, footer, form, h1, h2, h3, h4, h5, h6, header, hgroup, html, i, img, ins, label, li, mark, menu, nav, ol, p, pre, section, span, strong, sub, sup, table, tbody, td, th, thead, tr, tt, ul, var, video {
  margin: 0;
  padding: 0;
  border: 0;
  font: inherit;
  vertical-align: baseline;
}

*, *:before, *:after {
  box-sizing: border-box;
  transition: .1s ease-in-out;
}

ul {
  list-style: none;
}

a {
  text-decoration: none;
  outline: none;
}

img {
  display: block;
  width: 100%;
}

body {
  margin: 0;
  padding: 0;
  font-size: 18px;
  line-height: 24px;
  font-family: 'Open Sans', arial, sans-serif;
  color: #404040;
  background-color: white;
}

.container {
  margin: 0 auto;
  width: 100%;
  max-width: 1040px;
}

</style>
