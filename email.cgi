#!/usr/bin/perl -T
use strict;
use warnings;
use 5.008;
 
use Data::Dumper;
use CGI;
my $q = CGI->new;
 
my %data;
$data{name} = $q->param('name');
$data{email} = $q->param('email');
$data{message} = $q->param('message');
 
print $q->header;
if ($data{name} !~ /^[\s\w.-]+$/) {
	print "Name must contain only alphanumerics, spaces, dots and dashes.";
	exit;
}
 
# print "response " . Dumper \%data;
# print "Mail sent successfully";

# my %data;
# $data{name} = $q->param('name');
# $data{email} = $q->param('email');
# $data{message} = $q->param('message');

# if ($data{name} !~ /^[\s\w.-]+$/) {
#	print "Name must contain only alphanumerics, spaces, dots and dashes.";
#	exit;
# }

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
				
				<h1>Email Sent Successfully !!! &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br></h1>
				<h2>Thanks for getting in touch with us. We will contact you shortly...<br></h2>	
				<h3>Thanks for your time :D:D<br></h3>		<br><br><br><br>
				<div class="registration">
				<a href = "http://cs99.bradley.edu/~ysarwadia/bikers%20club/index.htm">Back</a>
				  <p>&nbsp;</p>
				</div>
			</div>
		</div>  <!-- end of body wrapper -->
	</div>Back
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



       









