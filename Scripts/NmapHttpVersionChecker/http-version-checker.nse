-- http-version-checker.nse

description = [[
    Sprawdza wersję serwera HTTP na określonym porcie.
]]

-- Definiowanie zależności
require 'http'
require 'shortport'

-- Lista portów, które są skanowane
portrule = shortport.http

-- Funkcja wywoływana przez Nmap dla każdego wykrytego portu
action = function(host, port)
    local path = "/"
    local status, response = http.get(host, port, path)

    if status and response then
        -- Przykład sprawdzenia nagłówka "Server" w odpowiedzi HTTP
        local server_header = response.header["server"]

        if server_header then
            return "Wersja serwera HTTP: " .. server_header
        else
            return "Nagłówek 'Server' nie znaleziony."
        end
    else
        return "Błąd podczas łączenia z portem."
    end
end
