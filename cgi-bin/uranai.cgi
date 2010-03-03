#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use HTML::Template;

my $q = CGI->new();
my $template = HTML::Template->new( filename => '../etc/uranai.html' );
my $name = $q->param('name');
if( $name ) {
    my $result = uranau( $name );
    $template->param( NAME => $name, RESULT => $result );
}else{
    $template->param( RESULT => '' );
}

print $q->header( { -type => 'text/html', -charset => 'utf8' } );
print $template->output;

sub uranau {
    my $name = shift;
    my @lists = get_lists();
    my $number = get_number( $name, $#lists + 1 );
    return $lists[$number];
}

sub get_number {
    my ($str, $max) = @_;
    my $num = 0;
    $num += ord( $_ ) for split //, $str;
    return $num % $max;
}

sub get_lists {
    my @lines = <DATA>;
    return @lines;
}

__DATA__
あなたは結婚できません。
あなたは不幸に会います。
あなたは貧乏になります。
あなたは事故にあいます。
あなたは死にます。
