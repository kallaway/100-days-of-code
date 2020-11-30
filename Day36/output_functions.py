def format_name(f_name, l_name):
  """This is a docString! Take a first and last name, format it to
  title case """
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  return f"{formatted_f_name} {formatted_l_name}"

formatted_string = format_name("WilliAM", "HALL")
print(formatted_string)
