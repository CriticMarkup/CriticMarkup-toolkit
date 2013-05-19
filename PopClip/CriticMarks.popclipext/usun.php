<?php
mb_internal_encoding("UTF-8");
$zaznaczenie=$_SERVER["POPCLIP_TEXT"];  
$dodajlewo="{++ ";
$dodajprawo="++}";	
$usunlewo="{-- ";
$usunprawo="--}";                   
$komlewo="{== ";
$komprawo="==}";
echo $usunlewo.$zaznaczenie.$usunprawo;  
?>