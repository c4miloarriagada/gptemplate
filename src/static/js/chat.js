'use strict'
;(() => {
  document.addEventListener('DOMContentLoaded', () => {
    const sendButton = document.getElementById('sendButton')
    const text = document.getElementById('text-box')
    const chatMessages = document.getElementById('chatMessages')
    const sendMessage = async () => {
      const message = text.value.trim()
      if (message !== '') {
        text.value = ''
        const data = await fetchtHandler({
          body: { message },
          method: 'POST',
          url: '/chat'
        })
      }
    }
    const textAreaHandler = () => {
      text.style.height = 'auto'
      text.style.height = text.scrollHeight + 'px'
    }
    text.addEventListener('input', textAreaHandler)
    sendButton.addEventListener('click', sendMessage)
  })
})()
