#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use HTML::Template;
use File::Slurp;

my $q = CGI->new();
my $template = HTML::Template->new( filename => 'uranai.html' );
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
    my @lists = @{ get_lists() };
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
    my @lines = read_file('uranai.txt');
    return \@lines;
}
