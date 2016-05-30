#!/usr/bin/perl -wT
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use Fcntl qw(:flock :seek);
use File::Basename;
use strict;
use Data::Dumper;


$CGI::POST_MAX = 1024 * 5000;

my $safe_filename_characters = "a-zA-Z0-9_.-";

my $upload_dir = "/home/ysarwadia/public_html/upload";

my $passfile = 'passwd.txt';
print header;
print start_html("Registration Results");
my $cgi = new CGI;

my %data;
$data{username} = $cgi->param('username');
$data{email} = $cgi->param('email');
$data{address} = $cgi->param('address');
$data{city} = $cgi->param('city');
$data{state} = $cgi->param('state');
$data{zip} = $cgi->param('zip');
$data{social_security} = $cgi->param('social_security');
$data{age} = $cgi->param('date');

$ENV{PATH} = '';
sendmail(
     $data{email},
    'Bikers Club Message',
     'Hello'. Dumper(\%data),
    'Bikers Club <sarwadiayukti@gmail.com>');
 
sub sendmail {
    my ($tofield, $subject, $text, $fromfield) = @_;
    my $mailprog = "/usr/lib/sendmail";
 
    open my $ph, '|-', "$mailprog -t -oi" or die $!;
    print $ph "To: $tofield\n";
    print $ph "From: $fromfield\n";
    print $ph "Reply-To: $fromfield\n";
    print $ph "Subject: $subject\n";
    print $ph "\n";
    print $ph "$text";
    close $ph;
    return ;
}

my $username = $cgi->param( "username" );
my $password = $cgi->param( "password" ); 
my $email = $cgi->param( "email" );
my $address = $cgi->param( "address" );
my $city = $cgi->param( "city" );
my $state = $cgi->param( "state" );
my $zip = $cgi->param( "zip" );
my $home_phone = $cgi->param( "home_phone" );
my $work_phone = $cgi->param( "work_phone" );
my $social_security = $cgi->param( "social_security" );
my $maiden_name = $cgi->param( "maiden_name" );
my $age = $cgi->param( "date" );
my $gender = $cgi->param( "gender" );
my $filename = $cgi->param("photo");

my @membership= $cgi->param( "activity");
my $membership2="";
foreach my $mem (@membership) {
   $membership2 .= "$mem ";
}

my @interests = $cgi->param( "interests" );
my $interests2="";
foreach my $interests (@interests) {
   $interests2 .= "$interests ";
}

# if ( !$filename )
# {
# print $cgi->header ( );
# print "There was a problem uploading your photo (try a smaller file).";
# exit;
# }

# my ( $name, $path, $extension ) = fileparse ( $filename, '..*' );
# $filename = $name . $extension;
# $filename =~ tr/ /_/;
# $filename =~ s/[^$safe_filename_characters]//g;


# if ( $filename =~ /^([$safe_filename_characters]+)$/ )
# {
# $filename = $1;
# }
# else
# {
# die "Filename contains invalid characters";
# }
# my $upload_filehandle = $cgi->upload("pic");
# open ( UPLOADFILE, ">$upload_dir/$filename" ) or die "$!";
# binmode UPLOADFILE;
# while ( <$upload_filehandle> )
# {
# print UPLOADFILE;
# }
# close UPLOADFILE;



my $salt = "21";
my $encpass = crypt($password,$salt);

open(PASSF,"+<$passfile") or &dienice("Can't open Details file.");
flock(PASSF, LOCK_EX);          # lock the file (exclusively)
seek(PASSF, 0, SEEK_SET);       # rewind to beginning
my @passf = <PASSF>;            # read entire file


seek(PASSF, 0, SEEK_END);       # go to EOF
print PASSF "$username:$encpass\n";
close(PASSF);



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
				<h2>User Name: $username &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</h2>
				<h2>Maiden Name: $maiden_name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</h2>
				<h2>Email: $email&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</h2>
				<h2>Address: $address&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</h2>
				<h2>City: $city&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</h2>
				<h2>State: $state&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</h2>
				<h2>Zip: $zip&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</h2>
				<h2>Home Phone: $home_phone&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</h2>
				<h2>Work Phone: $work_phone&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</h2>
				<h2>Social Security: $social_security&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</h2>
				<h2>Membership type: $membership2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</h2>
				<h2>Interest: $interests2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</h2>
				<h2>DOB: $age&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</h2>
				<h2>Gender: $gender&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</h2>
				<br/><h2>Details has been send your email id</h2>

				<div class="registration">
				<a href = "http://cs99.bradley.edu/~ysarwadia/bikers%20club/index.htm">Back</a>
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



sub dienice {
    my($msg) = @_;
    print "Error\n";
    print $msg;
    exit;
}
