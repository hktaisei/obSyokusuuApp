import binascii
import nfc
import csv
import subprocess

class TestCardReader(object):
  def on_connect(self, tag):
    print "touched"
    self.idm = binascii.hexlify(tag.idm)
    return True

  def read_id(self):
    clf = nfc.ContactlessFrontend('usb')
    try:
      clf.connect(rdwr={'on-connect' : self.on_connect})
    finally:
      clf.close()

if __name__ = '__main__':
  cr = TestCardReader()

  print "touch card:"
  cr.read_id()
  print "Separated"
  print cr.idm
  x = cr.idm

  file = open('test.txt', 'w')
  file.writeLines(x)
  file.close()

  if x = "カード固有のID":
    subprocess.call("aplay work24.wav", shell=True)
  elif x == "カード固有のID":
    subprocess.call("aplay test.wav", shell=True)
  elif x == "カード固有のID":
    subprocess.call("aplay teiji.wav", shell=True)
  else:
    subprocess.call("aplay hello.wav", shell=True)

  exit()