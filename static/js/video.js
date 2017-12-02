function main() {
  let video = document.getElementById('video')
  let canvas = document.createElement('canvas')

  let constraints = {
    audio: false,
    video: true
  }

  video.addEventListener('playing', (event) => {
    video.width = video.videoWidth
    video.height = video.videoHeight

    canvas.width = video.videoWidth
    canvas.height = video.videoHeight
  })

  navigator.mediaDevices.getUserMedia(constraints)
  .then((stream) => {
    video.srcObject = stream
    video.play()
  })


}

window.onload = main
