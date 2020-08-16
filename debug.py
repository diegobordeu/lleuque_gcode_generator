from gcode import GCode




gcode = GCode(49,19)
gcode.init_file()
gcode.build_file()

lines = gcode.get_gcode()
print('++++++++++++++++++++++++')
print('lines ----->', len(lines))
# print(lines.len)