import os 

print(("-"*20)+"\n")
max_wp_models=int(input("\nadd your max num of theme models:"))

html_cont_model="""
      <!DOCTYPE html>
<html lang="en">
<head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width',' initial-scale=1.0">
      <title>Document</title>
</head>
<header></header>
<body>

      <section class="sec1"></section>
      <section class="sec2"></section>
      <section class="sec3"></section>
            <scricpt src='model.js'></script>
</body>
<footer></footer>30
</html>
      """

php_cont_model="""
      <!DOCTYPE html>
<html lang="en">
<head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width',' initial-scale=1.0">
      <title>Document</title>
</head>
<header>
<?php get_header() ?>
</header>
<body>
<!--use-->
      <?php get_sidebar() ?>
      <!--or-->
<?php wp_nav_menu() ?>
      
      <section class="sec1"></section>
      <section class="sec2"></section>
      <section class="sec3"></section>
      <scricpt src='model.js'></script>
</body>
<footer>

<?php get_footer() ?>
</footer>
</html>
      """

css_media_query="""
@media (min-width:1440px) {}

@media (min-width:1025px) and (max-width:1439px) {}

@media (min-width:901px) and (max-width:1024px) {}

@media (min-width:601px) and (max-width:900px) {}

@media (max-width:600px) {}
"""
css_class_list=['ab-top-menu','sec1','sec2','sec3','pagenav','display-name','ab-sub-wrapper','searchform','screen-reader-shortcut','screen-reader-text','screen-reader-text','ab-icon','page_item page-item-2','page_item.page-item-18','page_item.page-item-22','page-template-default','page_item.page-item-20','page_item.page-item-3','ab-submenu','ab-top-menu','description','nojq.nojs']
css_id_list=['sidebar','searchform']
elem_list=['.pagenav>ul','ul[role="navigation"]','ul[role="navigation"]>li>h2','ul[role="navigation"]>li>ul']
php_files=['index','comments','404','footer','header','functions','search','single','page','singular','archive','front_page']
dir_list=['src','Classes','templates','theme-template','template-parts',]
sub_dir_list=['assets','css','fonts','images','javascript']
for f in range(max_wp_models):
      act1=os.mkdir("wp_theme_"+str(f+1))
      act2=os.system("nul>wp_theme_"+str(f+1)+"/style.css")
      act2_1=open("wp_theme_"+str(f+1)+"/style.css","w+")
      for c in range(len(css_class_list)):
            act2_1.write("."+css_class_list[c]+"{"+"}\n")
      for i in range(len(css_id_list)):
            act2_1.write("#"+css_id_list[i]+"{"+"}\n")
      for i in range(len(elem_list)):
            act2_1.write(""+elem_list[i]+"{"+"}\n")
      
      act2_1.write(css_media_query)
      act2_1.close()
      for p in range(len(php_files)):
       act3=os.system("nul>wp_theme_"+str(f+1)+"/"+php_files[p]+".php")
       act3_1=open("wp_theme_"+str(f+1)+"/"+php_files[p]+".php","w+")
       act3_1.write(php_cont_model)
       print(f"php {php_files[p]} file created \n")
       act3_1.close()

      act4=os.system("nul>wp_theme_"+str(f+1)+"/index.html")
      act4_1=open("wp_theme_"+str(f+1)+"/index.html","w+")
      act4_1.write(html_cont_model)
      act4_1.close()

      act5=os.system("nul>wp_theme_"+str(f+1)+"/model.js")
      act5_1=os.chdir("wp_theme_"+str(f+1))
      for d in range(len(dir_list)):
           act5_2=os.mkdir(dir_list[d])
      for d in range(len(sub_dir_list)):
           act5_3=os.mkdir(sub_dir_list[d])
           act5_4=os.chdir(sub_dir_list[d])
      for d in range(len(sub_dir_list)):
           act5_5=os.chdir("..")
      act6_1=os.chdir("..")
      
      

      






print(("-"*20)+"\n")