function main() {
  let video = document.getElementById('video');
  let canvas = document.createElement('canvas');
  let button = document.getElementById('take-pic');
  let registerFaceButton = document.getElementById('register-face');
  let checkFaceButton = document.getElementById('check-face');
  let info = document.getElementById('info-text');
  let facts = document.getElementById('facts');
  let item = document.getElementById('item');
  let nameInput = document.getElementById('name-input');

  let started = false;
  let sendRate = 7;// interval

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
      takeAndSendPicture(video, canvas, '/send-static-image', null, (response) => {
        item.innerHTML = '' + response.replace('_', ' ');
      })
    })

    registerFaceButton.addEventListener('click', () => {
      takeAndSendPicture(video, canvas, '/register-face', nameInput.value || 'Default')
    })

    checkFaceButton.addEventListener('click', () => {
      takeAndSendPicture(video, canvas, '/check-face', null, (response) => {
        info.innerHTML = 'Hello,'+ response + '!'
        console.log(response)
      })
    })
/*
    window.setInterval(() => {
      takeAndSendPicture(video, canvas, '/send-static-image', null, (response) => {
        info.innerHTML = 'What a nice ' + response.replace('_', ' ') + '!'
      })
    }, sendRate * 1000)*/
  })


  navigator.mediaDevices.getUserMedia(constraints)
  .then((stream) => {
    video.srcObject = stream
    video.play()
  })
}

function takeAndSendPicture(video, canvas, url, name, callback) {
  let data = { image: takePicture(video, canvas) }
  if (name) {
    data.name = name
  }
  sendPicture(data, url, callback)
}

function sendPicture(data, url, callback) {
  console.log('data sent to: '+url)

  $.post(url, data).done((response) => {
    console.log('response: '+response)
    if (callback) {
      callback(response)
    }
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
