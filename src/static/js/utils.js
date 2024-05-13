const fetchtHandler = async ({ body, method, url }) => {
  const req = await fetch(url, {
    headers: { 'Content-Type': 'application/json' },
    method,
    body: JSON.stringify(body)
  })

  const res = await req.json()

  return res
}
