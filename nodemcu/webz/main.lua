-- main.lua --
function blinktest()
    for i = 1, 10, 1 do       -- blink LED 50 times
    gpio.write(0, gpio.HIGH)  -- note onboard Blue LED is OFF when GPIO0 is high.
    gpio.write(1, gpio.HIGH)  -- RED LED is ON when GPIO1 is high.
     print("Red ON ",i)
    tmr.delay(500000) -- wait for 0.5 sec = 500 000 micro-sec
    gpio.write(0, gpio.LOW)  -- note onboard Blue LED is ON when GPIO0 is Low.
    gpio.write(1, gpio.LOW)  -- -- RED LED is OFF when GPIO1 is low.
      print("Red OFF ",i)
    i = i + 1;
    tmr.delay(500000)  -- wait for 0.5 sec = 500 000 micro-sec
    end
end

function testnodemcu()
  blinktest()
  tmr.delay(10000)  -- wait for 10micorsec
  print("Congratulations for your first successfull NODEMCU E12 LED blink Test")
  gpio.write(0, gpio.HIGH)  -- swtich OFF Blue LED at the end
end

-- Connect 
print('\nAll About Circuits main.lua\n')
tmr.alarm(0, 1000, 1, function()
   if wifi.sta.getip() == nil then
      print("Connecting to AP...\n")
   else
      ip, nm, gw=wifi.sta.getip()
      print("IP Info: \nIP Address: ",ip)
      print("Netmask: ",nm)
      print("Gateway Addr: ",gw,'\n')
      tmr.stop(0)
   end
end)

 -- Start a simple http server
srv=net.createServer(net.TCP)
srv:listen(80,function(conn)
  conn:on("receive",function(conn,payload)
    print(payload)
    conn:send("<h1> Hello, NodeMCU!!! </h1>")
    -- testnodemcu()  -- function to run the test script
    gpio.write(1, gpio.HIGH)  -- RED LED is ON when GPIO1 is high.
    print("Red ON ")
    tmr.delay(500000) -- wait for 0.5 sec = 500 000 micro-sec
    gpio.write(1, gpio.HIGH)  -- RED LED is ON when GPIO1 is high.
  end)
  conn:on("sent",function(conn) conn:close() end)
end)
