# args parser for cm to mm converter
parser.add_argument('--cm-to-mm', type=float, dest="cm_to_mm")

# helper function for checking args for cm_to_mm function
def cm_to_mm_helper():
    cm_mm = args.cm_to_mm
    if (cm_mm):
        cm_to_mm(cm_mm)

# function to convert cm to mm
def cm_to_mm(cm_mm):
    print(f'{cm_mm}cm in mm is: {cm*10} mm')
