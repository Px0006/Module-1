from notifiers import get_notifier

subprocess_cnt = 150
max_subprocess = 1000

while True:
  try:
    if subprocess_cnt <= max_subprocess:
      try:
        notifier.process_events()
        if notifier.check_events():
          notifier.read_events()
      except KeyboardInterrupt:
        notifier.stop()
        print('KeyboardInterrupt caught')
        raise  # the exception is re-raised to be caught by the outer try block
    else:
      pass
  except (KeyboardInterrupt, SystemExit):
    print('\nkeyboardinterrupt caught (again)')
    print('\n...Program Stopped Manually!')
    raise
