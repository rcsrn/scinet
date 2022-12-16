from random import randrange, choice
from datetime import timedelta, datetime
from django.core.management.base import BaseCommand, CommandError
from lorem_text import lorem
import names
from scinet_app.models import *

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

inst_init_date = datetime.strptime('1/1/1500 8:00 PM', '%m/%d/%Y %I:%M %p')
inst_final_date = datetime.strptime('1/1/2000 8:00 AM', '%m/%d/%Y %I:%M %p')

pub_init_date = datetime.strptime('1/1/1850 8:00 PM', '%m/%d/%Y %I:%M %p')
pub_final_date = datetime.strptime('12/15/2022 8:00 AM', '%m/%d/%Y %I:%M %p')

class Command(BaseCommand):
    help = 'Populates dabase with fake data: \n 10 topics, 50 institutions, 20 journals, 2000 publications, 200 users and 50 citations'
    
    topics = ['Mathematics', 'Computer Science', 'Biology', 'Physics', 
              'Psychology', 'Astronomy', 'Chemistry', 'Medicine', 
              'Engineering']
    
    countries = ['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe']
    
    gender = ['male', 'female']

    def handle(self, *args, **options):
        
        i = 0
        for topic in self.topics:
            i += 1
            t = Topic(topic_id=i, name=topic)
            t.save()
            
        for j in range(50):
            institution = Institution(institution_id=j, creation_date=random_date(inst_init_date, inst_final_date), country=choice(self.countries), name=lorem.words(5))
            institution.save()
            
        for j in range(20):
            journal = Journal(journal_id=j, name=lorem.words(2))
            journal.save()
            
        for j in range(100):
            journal = Journal.objects.get(journal_id=randrange(0,20))
            p = Publication(publication_id=j, journal_id=journal, title=lorem.words(10), publication_date=random_date(pub_init_date,pub_final_date),
                            content=lorem.paragraphs(20), doi=lorem.words(1))
            p.save()
            for k in range(randrange(1,5)):
                p.topic.add(Topic.objects.get(topic_id=randrange(0,9)))
                
        for j in range(100):
            first_name = names.get_first_name(gender=choice(self.gender))
            last_name = names.get_last_name()
            username = first_name + last_name
            user = GeneralUser(general_user_id=j, username=username, first_name=first_name, last_name=last_name, email=username + '@scinet.com',
                               password=lorem.words(1), age=randrange(18,100))
            user.save()
            for k in range(randrange(1,10)):
                user.publications.add(Publication.objects.get(publication_id=randrange(0,2000)))
            
            for k in range(randrange(1,5)):
                user.institutions.add(Institution.objects.get(institution_id=randrange(0,50)))
        
        for i in range(50):
            citer = Publication.objects.get(publication_id=randrange(0,100))
            citee = Publication.objects.get(publication_id=randrange(0,100))
            citation = Citations(citer=citer, citee=citee)
            citation.save()
        