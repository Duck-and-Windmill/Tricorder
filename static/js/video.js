'use strict'

function main() {
  let video = document.getElementById('video')
  let canvas = document.getElementById('canvas')
  let started = false
  let sendRate = 3 // send rate per second

  let constraints = {
    audio: false,
    video: true
  }

  video.addEventListener('playing', (event) => {
    if (started) return

    started = true

    let width = video.videoWidth
    let height = video.videoHeight

    video.width = width
    video.height = height

    canvas.width = width
    canvas.height = height

    let context = canvas.getContext('2d')
    context.drawImage(video, 0, 0, width, height)
    let data = canvas.toDataURL('image/jpeg')

    $.post('/sendStaticImage', {
      image : data
    }).done(function(response) {
      // alert('Server returned: ' + response);
    }).fail(function() {
      console.log('failed to return results');
    });

    window.setInterval(() => {
      let context = canvas.getContext('2d')
      context.drawImage(video, 0, 0, width, height)
      let data = canvas.toDataURL('image/jpeg')

      console.log(data)

      $.post('/sendStaticImage', {
        image : data
      }).done(function(response) {
        console.log('returned: '+response.data)
      }).fail(function() {
        console.log('failed to return results');
      });
    }, sendRate * 1000)
  })

  navigator.mediaDevices.getUserMedia(constraints)
  .then((stream) => {
    video.srcObject = stream
    video.play()
  })
}

window.onload = main
