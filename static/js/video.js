function main() {
  let video = document.getElementById('video')
  let canvas = document.getElementById('canvas')
  let button = document.getElementById('button')
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
      takePicture(video, canvas)
    })

    let data = takePicture(video, canvas)

    $.post('/sendStaticImage', {
      image : data
    }).done((response) => {
      // alert('Server returned: ' + response);
    }).fail(() => {
      console.log('failed to return results');
    })

    window.setInterval(() => {
      let data = takePicture(video, canvas)

      $.post('/send_static_image', {
        image : data
      }).done((response) => {
        console.log('returned: '+response.data)
      }).fail(() => {
        console.log('failed to return results')
      })
    }, sendRate * 1000)
  })

  navigator.mediaDevices.getUserMedia(constraints)
  .then((stream) => {
    video.srcObject = stream
    video.play()
  })
}

function takePicture(video, canvas) {
  let context = canvas.getContext('2d')
  context.drawImage(video, 0, 0, canvas.width, canvas.height)
  let data = canvas.toDataURL('image/jpeg')

  return data
}

window.onload = main
