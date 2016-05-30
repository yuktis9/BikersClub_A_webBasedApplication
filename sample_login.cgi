#!/usr/bin/perl -wT
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use Fcntl qw(:flock :seek);
use strict;

print "Content-type: text/html\n\n";

my $passfile = 'passwd.txt';
print header;
print start_html("Registration Results");

my $cgi = new CGI;

            my $Uname = $cgi->param( "Uname" );
            my $password1 = $cgi->param( "pword1" );





# my $encpass = &encrypt($password1);
# &dienice("Half script read");

my $salt = "21";
my $enpass = crypt($password1,$salt);

open(PASSF,"+<$passfile") or &dienice("Can't open Details file.");
flock(PASSF, LOCK_EX);          # lock the file (exclusively)
seek(PASSF, 0, SEEK_SET);       # return to the beginning
my @passf = <PASSF>;            # read entire file

# the structure of the file is:
# username:passwd:email
# username:passwd:email
# with each user's record on a separate line.
# here we're going to loop through and make sure the new username
# doesn't already exist in the file.


my $flag = "true";

foreach my $i (@passf) {
    chomp($i);
    my ($User,$pass) = split(/:/,$i);
    if ($User eq $Uname && $pass eq $enpass) {

	$flag = "false";


print <<END_HTML;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<head>
	<title>Bikers</title>
	<link href="http://cs99.bradley.edu/~ysarwadia/bikers%20club/css/style.css" rel="stylesheet" type="text/css" />
    <style type="text/css">
<!--
.style12 {color: #FF00FF}
.style7 {color: #FFFFFF}
.style16 {color: #c1c1c1; font-weight: bold; }
.style17 {color: #c1c1c1}
.style1 {	font-family: Georgia, "Times New Roman", Times, serif;
	color: #FF00FF;
}
.style3 {color: #FF00FF; }
-->
    </style>
</head>

<body>
	<div id="page">
		<div id="header"> <!-- start of header -->
			<ul>
				<li><a href="index.htm">Home</a></li>
				<li></li>
				<li><a href="events.htm">Events</a></li>
				<li><a href="gallery.htm">Gallery</a></li>
				<li><a href="blog.htm">Login</a></li>
				<li><a href="contact-us.htm">Contact</a></li>
			</ul>

			<div>
				<a href="register.htm" class="join"></a>
				<h3>Press To Join the Club .. </h3>
				</div>
		</div> <!-- end of header -->

		<div id="body">  
			<div class="contents">
				
				<h1>Welcome $Uname to Biker's Club &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</h1>
				<div class="registration">
				<a href = "http://cs99.bradley.edu/~ysarwadia/bikers%20club/index.htm">Logout</a>
				  <p>&nbsp;</p>
				</div>
			</div>
		</div>  <!-- end of body wrapper -->
	</div>
	<div id="footer"> <!-- start of footer part -->
		<div>
			<ul>
				<li><a href="http://facebook.com" target="_blank" class="fb">Facebook</a></li>
				<li><a href="http://twitter.com" target="_blank" class="twitr">Twitter</a></li>
			</ul>
			<span> &copy; Copyright &copy; 2010. <a href="index.htm">Company name.</a> All Rights Reserved </span>
		</div>
	</div> <!-- end of footer part -->
</body>
</html>






END_HTML



       











seek(PASSF, 0, SEEK_END);       # go to EOF
close(PASSF);
   }

}

if($flag eq "true"){

print qq(<p> Either your uname or password or both either do not exist or do not match the existing data. 
	Try again.</p>\n);

}


#seek(PASSF, 0, SEEK_END);       # go to EOF
#print PASSF "$Uname:$password1\n";
#close(PASSF);



#print end_html;



sub dienice {
    my($msg) = @_;
    print "<h2>Error</h2>\n";
    print $msg;
    exit;
}
