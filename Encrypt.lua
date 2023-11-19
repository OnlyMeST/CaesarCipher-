  local Convert = function (Text, Action, Shift)
    -- Define a nested function called "Check" that checks if a character is uppercase or lowercase.
    local function Check(C)
      if string.byte(C) >= 65 and string.byte(C) <= 90 then
        return "U"
      elseif string.byte(C) >= 97 and string.byte(C) <= 122 then
        return "L"
      end
    end
  
    -- Ensure Shift is within the range [1, 26] to handle rotations.
    Shift = Shift % 26
    if Shift == 0 then
      Shift = 26
    end

    local Enc = function (a, b)
      local Byte = (string.byte(a) - b + Shift) % 26
      if Byte == 0 then
        Byte = 26
      end
      return string.char(Byte + b)
    end

    local Dec = function (a, b)
      local Byte = (string.byte(a) - b - Shift) % 26
      if Byte == 0 then
        Byte = 26
      end
      return string.char(Byte + b)
    end
  
    -- Initialize an empty string "E" and a variable "Activity" based on the "Action" parameter.
    local E, Activity = ""
    if tostring(Action) == "Enc" then
      Activity = Enc
    elseif tostring(Action) == "Dec" then
      Activity = Dec
    else
      print("Error : Action Not Selected")
      os.exit()
    end
  
    for I = 1, #Text do
      local C = string.sub(Text, I, I)
      local Checked = Check(C)
      if Checked == "U" then
        E = E .. Activity(C, 64) -- Uppercase letter encoding/decoding.
      elseif Checked == "L" then
        E = E .. Activity(C, 96) -- Lowercase letter encoding/decoding.
      else
        E = E .. C -- Non-alphabetical characters remain unchanged.
      end
    end
  
    -- Return the encoded or decoded result.
    return E
  end
  

  local random = math.random(1,26)
  print('Enter your Text:')
  local String = io.read()
  local Enc = Convert(String, "Enc", random)
  local Dec = Convert(Enc, "Dec", random)
  print("Encoded : " .. Enc .. "\nDecoded : " .. Dec .. "\n Key : " .. random)
  