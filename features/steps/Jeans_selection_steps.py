from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given,when,then

colors_jeans = ['Black','Blue Overdyed','Dark Wash','Indigo Wash','Light Vintage','Light Wash',
          'Medium Vintage','Medium Wash','Rinse','Rinsed Vintage','Vintage Light Wash','Washed Black',
          'Bright White','Dark Khaki','Light Khaki','Olive','Sage Green']

Color_Option = (By.CSS_SELECTOR,"div#variation_color_name li")
Selected_color = (By.CSS_SELECTOR,"div#variation_color_name span.selection")


@given ("Open Amazon jeans {product} page")
def Jeans_page (context,product):
    context.driver.get(f'https://www.amazon.com/gp/product/{product}')


@then ("Verify User can select through colors")
def Verify_jeans_colors(contect):
    colors = contect.driver.find_elements(*Color_Option)
    for i in range(len(colors)):
        colors[i].click()
        color_text = contect.driver.find_element(*Selected_color).text
        assert color_text==colors_jeans[i],\
            f"Color don't match. Expected color: {colors_jeans[i]}, but got: {color_text}"
