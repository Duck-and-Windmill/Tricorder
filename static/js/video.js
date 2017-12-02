'use strict'

function main() {
  let video = document.getElementById('video')
  let canvas = document.createElement('canvas')
  let started = false
  let sendRate = 5 // send rate per second

  let constraints = {
    audio: false,
    video: true
  }

  video.addEventListener('playing', (event) => {
    if (started) return

    started = true

    video.width = video.videoWidth
    video.height = video.videoHeight

    canvas.width = video.videoWidth
    canvas.height = video.videoHeight

    window.setInterval(() => {
      let context = canvas.getContext('2d')
      context.drawImage(video, 0, 0, width, height)
      data = canvas.toDataURL('image/jpg')

      post('/sendStaticImage', {
        image: data
      }, () => {
        console.log('done')
      })
    }, sendRate * 1000)
  })

  navigator.mediaDevices.getUserMedia(constraints)
  .then((stream) => {
    video.srcObject = stream
    video.play()
  })
}

function post(url, data) {
  return new Promise((resolve, reject) => {
    let request = new XMLHttpRequest();
    request.open('POST', url, true);
    request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');

    request.addEventListener('readystatechange', (event) => {
      if (this.readyState == XMLHttpRequest.DONE && this.status == 200) {
        resolve(event.responseText)
      }
      else {
        reject()
      }
    }

    request.send(data);
  })
}

window.onload = main
