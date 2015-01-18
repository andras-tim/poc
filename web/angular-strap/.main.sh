### Main ###

function get_commands()
{
    declare -F | grep '^declare -f do_' | sed 's>^.*do_>>'
}

function show_help()
{
    cat - << EOF
$(basename "$0") command [arg]

Available commands:
$(get_commands | sort | sed 's>^>  * >')

Available arguments:
  -h, --help            Show this help

EOF
}


# Init
cmd=
while [ $# -gt 0 ]
do
    case "$1" in
        --help|-h)          show_help
                            exit 0
                            ;;
        *)                  if [ "${cmd}" == '' ]
                            then
                                if get_commands | grep -qx -- "$1"
                                then
                                    cmd="$1"
                                else
                                    echo "Unknown command: $1" >&2
                                    exit 1
                                fi
                            else
                                echo "Unknown parameter: $1" >&2
                                exit 1
                            fi
                            ;;
    esac
    shift
done
if [ "${cmd}" == '' ]
then
    echo "Missing command parameter!" >&2
    show_help
    exit 1
fi


# Start
do_${cmd}
exit 0
