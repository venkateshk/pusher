import pusher

p = pusher.Pusher(
  app_id='140107',
  key='3f344b89f59af5cd7cc1',
  secret='41325f033451e0187b4b',
  ssl=True,
  port=443
)
p.trigger('test_channel', 'my_event', {'message': '17.6883,83.2186'})
