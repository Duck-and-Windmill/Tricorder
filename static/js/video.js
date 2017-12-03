function main() {
  let video = document.getElementById('video')
  let canvas = document.getElementById('canvas')
  let button = document.getElementById('button')
  let registerFaceButton = document.getElementById('register-face')

  let started = false
  let sendRate = 8 // interval

  let constraints = {
    audio: false,
    video: true
  }

  video.addEventListener('playing', (event) => {
    if (started) {
      return
    }
    started = true

    let width = video.videoWidth
    let height = video.videoHeight

    video.width = width
    video.height = height

    canvas.width = width
    canvas.height = height

    button.addEventListener('click', () => {
      takeAndSendPicture(video, canvas, '/send-static-image')
    })

    registerFaceButton.addEventListener('click', () => {
      takeAndSendPicture(video, canvas, '/register-face', 'Michael')
    })
  })

  navigator.mediaDevices.getUserMedia(constraints)
  .then((stream) => {
    video.srcObject = stream
    video.play()
  })
}

function takeAndSendPicture(video, canvas, url, name) {
  let data = { image: takePicture(video, canvas) }
  if (name) {
    data.name = name
  }
  sendPicture(data, url)
}

function sendPicture(data, url) {
  console.log('data sent to: '+url)

  $.post(url, data).done((response) => {
    console.log('response: '+response)
  }).fail(() => {
    console.log('failed to return results');
  })
}

function takePicture(video, canvas) {
  console.log('picture taken!')

  let context = canvas.getContext('2d')
  context.drawImage(video, 0, 0, canvas.width, canvas.height)
  let data = canvas.toDataURL('image/jpeg')

  return data
}

window.onload = main
