redled = 1
whiteled = 2

gpio.mode(redled, gpio.OUTPUT)
gpio.mode(whiteled, gpio.OUTPUT)

srv=net.createServer(net.TCP)
srv:listen(80,function(conn)
    conn:on("receive", function(client,request)
        local buf = "";
        local _, _, method, path, vars = string.find(request, "([A-Z]+) (.+)?(.+) HTTP");
        if(method == nil)then
            _, _, method, path = string.find(request, "([A-Z]+) (.+) HTTP");
        end
        local _GET = {}
        if (vars ~= nil)then
            for k, v in string.gmatch(vars, "(%w+)=(%w+)&*") do
                _GET[k] = v
            end
        end
        buf = buf.."<h1>ESP8266 Web Server</h1>";
        buf = buf.."<p>White led <a href=\"?pin=ONRED\"><button>ON</button></a>&nbsp;<a href=\"?pin=OFFRED\"><button>OFF</button></a></p>";
        buf = buf.."<p>Red led <a href=\"?pin=ONWHITE\"><button>ON</button></a>&nbsp;<a href=\"?pin=OFFWHITE\"><button>OFF</button></a></p>";
        local _on,_off = "",""
        if(_GET.pin == "ONRED")then
              gpio.write(redled, gpio.HIGH);
        elseif(_GET.pin == "OFFRED")then
              gpio.write(redled, gpio.LOW);
        elseif(_GET.pin == "ONWHITE")then
              gpio.write(whiteled, gpio.HIGH);
        elseif(_GET.pin == "OFFWHITE")then
              gpio.write(whiteled, gpio.LOW);
        end
        client:send(buf);
        client:close();
        collectgarbage();
    end)
end)
