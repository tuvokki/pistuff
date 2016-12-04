powerpin = 1

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
        buf = buf.."<!DOCTYPE html>";
        buf = buf.."<html lang=\"en\">";
        buf = buf.."<head>";
        buf = buf.."<meta charset=\"utf-8\">";
        buf = buf.."<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">";
        buf = buf.."<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">";
        buf = buf.."<title>Button</title>";
        buf = buf.."<link href=\"http://netdna.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap.min.css\" rel=\"stylesheet\">";
        buf = buf.."</head>";
        buf = buf.."<body id=\"page-top\">";
        buf = buf.."<div class=\"jumbotron\">";
        buf = buf.."<h1>This is a switch</h1>";
        buf = buf.."<p>Just a simple on off switch</p>";
        buf = buf.."<div class=\"btn-group\" role=\"group\" aria-label=\"switch\">";
        -- read value of gpio 0.
        if (gpio.read(powerpin) == gpio.LOW)then
            buf = buf.."<a href=\"?pin=POWERON\" class=\"btn btn-default btn-xl\">ON</a>";
            buf = buf.."<a href=\"?pin=POWEROFF\" class=\"btn btn-danger btn-xl\">OFF</a>";
        else
            buf = buf.."<a href=\"?pin=POWERON\" class=\"btn btn-primary btn-xl\">ON</a>";
            buf = buf.."<a href=\"?pin=POWEROFF\" class=\"btn btn-default btn-xl\">OFF</a>";
        end
        buf = buf.."</div>";
        buf = buf.."</div>";
        buf = buf.."</body>";
        buf = buf.."</html>";
        local _on,_off = "",""
        if (_GET.pin == "POWEROFF")then
            gpio.write(powerpin, gpio.HIGH);
        elseif (_GET.pin == "POWERON")then
            gpio.write(powerpin, gpio.LOW);
        end
        client:send(buf);
        client:close();
        collectgarbage();
    end)
end)
