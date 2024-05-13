'use strict'
;(() => {
  document.addEventListener('DOMContentLoaded', () => {
    const sendButton = document.getElementById('sendButton')
    const input = document.getElementById('text')
    const chatMessages = document.getElementById('chatMessages')
    const sendMessage = async () => {
      const message = input.value.trim()
      if (message !== '') {
        input.value = ''
        const data = await fetchtHandler({
          body: { message },
          method: 'POST',
          url: '/chat'
        })
      }
    }
    sendButton.addEventListener('click', sendMessage)
  })
})()
