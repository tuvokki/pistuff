LED_PIN = 1

gpio.mode(LED_PIN, gpio.OUTPUT)

d1status=gpio.read(1)
print ("D1 status before: "..d1status)
if d1status == 0 then
  gpio.write(LED_PIN, gpio.HIGH)
else
  gpio.write(LED_PIN, gpio.LOW)
end

d1status=gpio.read(1)
print ("D1 status after: "..d1status)
