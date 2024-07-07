import os,shutil 

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


php_header_model="""
<html <?php language_attributes();?>>
<head>
      <meta <?php bloginfo('charset');?>>
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <?php wp_head();?>
      <title>Document</title>
</head>
<header><div><h1>this is header</h1></div></header>
<body <?php body_class();?>>

"""

php_footer_model="""
<div><h4>this is footer</h4></div>
</body>
<?php wp_footer(); ?>
</html>

"""


php_key="""
<?php    











?>
"""


css_theme_info="""

/**
Theme Name:Manjaka
Theme URI:http://Manjaka.com
Author:Mohamed sabry
Author URI :http://Manjaka.com
Theme Name:Manjaka
Theme Name:Manjaka
Version:1.0.0
Description:Mekanolova Sis



**/
"""

css_media_query="""
@media (min-width:1440px) {}

@media (min-width:1025px) and (max-width:1439px) {}

@media (min-width:901px) and (max-width:1024px) {}

@media (min-width:601px) and (max-width:900px) {}

@media (max-width:600px) {}
"""
php_make_post_model="""<div id="post-<?php the_ID(); ?>">
      <h1>the post <?php the_ID(); ?>:<?php the_title('<a class="entry-link" href="'.esc_url( get_permalink() ).'">','</a>')?> </h1>
      <p>

      <?php 
      if (has_post_thumbnail()):
            the_post_thumbnail('large');
      endif;
      
      ?>
      </p>
      <h3>
      <?php 
      the_excerpt();
      ?>
      </h3>
</div> """
php_view_post_model="""

<?php    


get_header();

if (have_posts()):
      while (have_posts()):
            the_post();
            the_content();
      endwhile;
endif;

get_footer();
?>
<h1>this is Post model</h1>
 """
php_add_post_content=""" """


css_class_list=['ab-top-menu','sec1','sec2','sec3','pagenav','display-name','ab-sub-wrapper','searchform','screen-reader-shortcut','screen-reader-text','screen-reader-text','ab-icon','page_item page-item-2','page_item.page-item-18','page_item.page-item-22','page-template-default','page_item.page-item-20','page_item.page-item-3','ab-submenu','ab-top-menu','description','nojq.nojs']
css_id_list=['sidebar','searchform']
elem_list=['.pagenav>ul','ul[role="navigation"]','ul[role="navigation"]>li>h2','ul[role="navigation"]>li>ul']
php_files=['index','comments','404','footer','header','functions','search','single','page','singular','archive','front_page']
dir_list=['inc','Classes','templates','theme-template','template-parts',]
sub_dir_list=['assets','css','fonts','images','javascript']
for f in range(max_wp_models):
  act_1=os.mkdir("wp_theme_no_"+str(f+1))
  cp=shutil.copy2('Screenshot.jpg','wp_theme_no_'+str(f+1)+'/Screenshot.png')
  act_2=os.chdir("wp_theme_no_"+str(f+1))
  act_1=os.mkdir("inc")
  act_1=os.mkdir("template-parts")
  act_1=os.chdir("template-parts")
  act_1=os.mkdir("posts")
  act_1=os.mkdir("pages")
  act_1=os.system("nul>posts/content.php")
  act_1=os.system("nul>pages/content-page.php")
  act_1=os.system("nul>pages/content-none.php")
  act_2_cont=open("posts/content.php",'w+')
  act_2_cont.write(php_make_post_model)
  act_2_cont.close()
  act_1=os.chdir("..")
  #act_1=os.chdir("..")
  #act_1=os.mkdir("inc")
  act_2_1=os.system("nul>style.css")
  act_2_2=open("style.css",'w+')
  act_2_2.write(f"""
/**
Theme Name:Manjaka-{f}
Theme URI:http://Manjaka.com
Author:Mohamed sabry
Author URI :http://Manjaka.com
Theme Name:Manjaka
Theme Name:Manjaka
Version:1.0.0
Description:Mekanolova Sis



**/

   """)
  act_2_2.write(css_media_query)
  act_2_2.close()
  for f_item in range(len(php_files)):
    act_3=os.system("nul>"+php_files[f_item]+".php")
    print("file "+php_files[f_item]+".php created")
    if php_files[f_item] == "header":
      print("HEADER FOUND")
      act_3_1=open(php_files[f_item]+".php","+w")
      act_3_1.write(php_header_model)
      act_3_1.close()
    elif php_files[f_item] == "footer":
      print("FOOTER FOUND")
      act_3_1=open(php_files[f_item]+".php","+w")
      act_3_1.write(php_footer_model)
      act_3_1.close()
    elif php_files[f_item] == "single":
      print("SINGLE FOUND")
      act_3_1=open(php_files[f_item]+".php","+w")
      act_3_1.write(php_view_post_model)
      act_3_1.close()
    else :
      act_3_1=open(php_files[f_item]+".php","+w")
      act_3_1.write(php_key)
      act_3_1.close()

  act_4=os.chdir("..")
act_4=os.chdir("..")
    
      






print(("-"*20)+"\n")