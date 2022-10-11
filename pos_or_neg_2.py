#!/usr/bin/env python3
import sys
count = int(sys.argv[1])
if count > 0:
  message = 'it is positive!'
  if count < 50:
    message2 = 'and it is less than 50'
    if (count % 2) == 0:
        message3 = ', oh yeah and it is even'
        print(count, message, message2, message3)
    else:
        message3 = ', oh yeah and it is odd'
        print(count, message, message2, message3)
  elif count > 50:
    message2 = 'and it is greater than 50'
    if (count % 2) == 0:
      message3 = ', oh yeah and it is even'
      if (count % 3) == 0:
        message4 = ', yep, it is divisible by 3'
        print(count, message, message2, message3, message4)
      else:
        print(count, message, message2, message3)
    else:
      message3 = ', oh yeah and it is odd'
      if (count % 3) == 0:
        message4 = ', yep, it is divisible by 3'
        print(count, message, message2, message3, message4)
      else:
        print(count, message, message2, message3)
elif count < 0:
  message = 'it is negativo! and less than 50'
  print(count, message)
  if (count % 2) == 0:
      message3 = ', oh yeah and it is even'
      print(count, message, message3)
  else:
      message3 = ', oh yeah and it is odd'
      print(count, message, message3)
elif count == 0:
  message = 'it must be zero! and less than 50'
  print(count, message)
