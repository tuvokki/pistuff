-- main.lua --

-- Connect 

tmr.alarm(0, 1000, 1, function()
   if wifi.sta.getip() == nil then
      print("Connecting...\n")
   else
      ip, nm, gw=wifi.sta.getip()
      print("Connected with IP Address: ",ip)
      tmr.stop(0)
   end
end)

 -- Start a simple http server
srv=net.createServer(net.TCP)
srv:listen(80,function(conn)
  conn:on("receive",function(conn,payload)
    print(payload)
    conn:send("<h1> Hello, NodeMCU!!! </h1>")
    gpio.write(1, gpio.HIGH)  -- RED LED is ON when GPIO1 is high.
    tmr.delay(500000) -- wait for 0.5 sec = 500 000 micro-sec
    gpio.write(1, gpio.LOW)  -- RED LED is ON when GPIO1 is high.
  end)
  conn:on("sent",function(conn) conn:close() end)
end)
