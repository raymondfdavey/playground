#! /bin/bash
# https://askubuntu.com/questions/1705/how-can-i-create-a-select-menu-in-a-shell-script
echo "hello world"
read -p "enter your age: " age
echo "you entered $age"

PS3='Please enter your choice: '
options=("Option 1" "Option 2" "Option 3" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "Option 1")
            echo "you chose choice 1"
            ;;
        "Option 2")
            echo "you chose choice 2"
            ;;
        "Option 3")
            echo "you chose choice $REPLY which is $opt"
            ;;
        "Quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done

title="Select example"
prompt="Pick an option:"
options=("A" "B" "C")

echo "$title"
PS3="$prompt "
select opt in "${options[@]}" "Quit"; do 
    case "$REPLY" in
    1) echo "You picked $opt which is option 1";;
    2) echo "You picked $opt which is option 2";;
    3) echo "You picked $opt which is option 3";;
    $((${#options[@]}+1))) echo "Goodbye!"; break;;
    *) echo "Invalid option. Try another one.";continue;;
    esac
done

while opt=$(zenity --title="$title" --text="$prompt" --list \
                   --column="Options" "${options[@]}")
do
    case "$opt" in
    "${options[0]}") zenity --info --text="You picked $opt, option 1";;
    "${options[1]}") zenity --info --text="You picked $opt, option 2";;
    "${options[2]}") zenity --info --text="You picked $opt, option 3";;
    *) zenity --error --text="Invalid option. Try another one.";;
    esac
done


