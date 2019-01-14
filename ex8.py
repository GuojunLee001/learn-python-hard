# _*_ coding: utf-8 _*_

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)
# 最后一行打印出来有双单引号原因：内部含有一个‘ ，避免混淆，所有变为“ ”
print formatter % (
  "I had this thing.",
  "That you could type up right.",
  "But it didn't sing.",
  "So I said goodnignt."
  )