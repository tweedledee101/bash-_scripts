#start of file, want to bring a file from one directory into the directory we are currently in. 
hello="hello_world"
echo $hello
echo "currently you are in:"

directory=$(pwd)
echo "${directory}"



echo "would you like to import a file into this directory?"
echo "[1]:yes [2]:no"
read file_import_answer

if [[($file_import_answer -eq 1)]];
    then
        echo "great, let's continue"
        echo "file name?"

        read file_name

        printf "\nsearching for:\n"
        echo $file_name

        echo""
        echo "switching to / directory"
        cd /

        found_location=$(find . -name "$file_name")
        for location in $found_location
        do
        #echo "found location"
        #echo $location
        file_locations+=($location)
        done
        echo "${#file_locations[@]}"

        if [[(${#file_locations} -gt 0)]];
        then 
            printf "\nFound these matching files:\n"
            COUNTER=0
            for file in ${file_locations[@]};
                do
                printf $COUNTER
                echo $file
                let COUNTER++
                done
        else
            printf "\nno files found \n"
        fi

        echo "Which path would you like to copy file from? (answers must be an integer i.e. [1], [2], [3], etc.)"
        read file_path_answer
        file_selection=${file_locations[$file_path_answer]}
        echo "You Chose: $file_selection"
        cp $file_selection $directory
        echo "file is now copied"
        cd $directory
        ls
        exit 0



else 
    echo "ok, thanks for coming"
fi
exit 1

