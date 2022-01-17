:- dynamic(prop/3).

%-----------------------------------------------------------------------------------------------------------------------
% RULES

% Definizione di classe
prop(X, type, C) :-
    prop(S, subClassOf, C),
    prop(X, type, S).

% Definisce il numero massimo di dipendenti all'interno dell'azienda e quanti posti disponibili ci sono per le assunzioni
prop(dipendentiDaAssumere, availability, N):-
    prop(postiLavoro, total, D),
    D >= N.

% Mostra le figure presenti all'interno dell'azienda. Se ne manca qualcuna ti suggerisce di assumerla
prop(E, list_of_employees, true):-
    prop(E, type, staff),
    prop(E, availability, N),
    N > 0.

prop(E, list_of_employees, false):-
    prop(E, type, staff),
    prop(E, availability, N),
    N=:=0.
%----------------------------------------------------------------------------------------------------------------------
% DATA

% STAFF AZIENDALE
prop(ceo, type, staff).
prop(cto, type, staff).
prop(co_founder, type, staff).
prop(project_manager, type, staff).
prop(scrum_master, type, staff).
prop(team_leader, type, staff).
prop(lead_developer, type, staff).
prop(frontend_developer, type, staff).
prop(backend_developer, type, staff).
prop(analist, type, staff).
prop(senior_developer, type, staff).
prop(developer, type, staff).
prop(junior_developer, type, staff).
prop(recruiter, type, staff).
prop(intern, type, staff).

% POSTI OCCUPATI ALL'INTERNO DELL'AZIENDA
prop(ceo, availability, 1).
prop(cto, availability, 1).
prop(co_founder, availability, 4).
prop(project_manager, availability, 10).
prop(scrum_master, availability, 15).
prop(team_leader, availability, 10).
prop(lead_developer, availability, 40).
prop(frontend_developer, availability, 70).
prop(backend_developer, availability, 80).
prop(analist, availability, 150).
prop(senior_developer, availability, 100).
prop(developer, availability, 450).
prop(junior_developer, availability, 300).
prop(recruiter, availability, 0).
prop(intern, availability, 0).

%----------------------------------------------------------------------------------------------------------------------
% RULES FOR PROJECTS
%il progetto richiede un determinato linguaggio
prop(P, requires, L):-
    prop(P, type, project),
    prop(project, requires, L).

%il linguaggio è richiesto nel progetto
prop(L, is_required, P):-
    prop(P, requires, L),
    prop(L, subClassOf, ittechnology).

%figura che lavora al progetto
prop(E, work, P):-
    prop(P, requires, E),
    prop(P, type, project),
    prop(E, subClassOf, staff).
%----------------------------------------------------------------------------------------------------------------------
% TECHNOLOGIES USED
prop(language, subClassOf, itTechnology).
prop(database, subClassOf, itTechnology).
prop(framework, subClassOf, itTechnology).

prop(python, type, language).
prop(java, type, language).
prop(javascript, type, language).
prop(mysql, type, database).
prop(mongodatabase, type, database).
prop(html, type, language).
prop(angular, type, framework).
prop(c, type, language).
prop(cplusplus, type, language).
prop(firebase, type, database).


% LIST OF PROJECT WITH THEIR REQUIREMENT
prop(application_enel, subClassOf, project).
prop(application_enel, requires, python).
prop(application_enel, requires, mongodatabase).

prop(application_modis, subClassOf, project).
prop(application_modis, requires, java).
prop(application_modis, requires, mysql).
prop(application_modis, requires, mongodatabase).

prop(project_for_region, subClassOf, project).
prop(project_for_region, requires, javascript).
prop(project_for_region, requires, java).
prop(project_for_region, requires, angular).

prop(project_for_university_of_bari, subClassOf, project).
prop(project_for_university_of_bari, requires, python).
prop(project_for_university_of_bari, requires, mysql).

prop(deployement_newere, subClassOf, project).
prop(deployement_newere, requires, html).
prop(deployement_newere, requires, angular).

prop(project_for_fabio, subClassOf, project).
prop(project_for_fabio, requires, python).
prop(project_for_fabio, requires, java).
prop(project_for_fabio, requires, html).
prop(project_for_fabio, requires, javascript).

prop(deployement_for_clobetasolo, subClassOf, project).
prop(deployement_for_clobetasolo, requires, mysql).
prop(deployement_for_clobetasolo, requires, mongodatabase).

prop(project_for_pippo, subClassOf, project).
prop(project_for_pippo, requires, python).
prop(project_for_pippo, requires, mongodatabase).
prop(project_for_pippo, requires, html).

prop(python, is_required, project_for_pippo).
prop(python, is_required, project_for_university_of_bari).
prop(python, is_required, project_for_fabio).
prop(python, is_required, application_enel).

prop(java, is_required, application_modis).
prop(java, is_required, project_for_region).
prop(java, is_required, project_for_fabio).

prop(javascript, is_required, project_for_region).
prop(javascript, is_required, project_for_fabio).

prop(mysql, is_required, application_modis).
prop(mysql, is_required, project_for_university_of_bari).
prop(mysql, is_required, deployement_for_clobetasolo).

prop(mongodatabase, is_required, application_enel).
prop(mongodatabase, is_required, application_modis).
prop(mongodatabase, is_required, deployement_for_clobetasolo).
prop(mongodatabase, is_required, project_for_pippo).

prop(html, is_required, deployement_newere).
prop(html, is_required, project_for_fabio).
prop(html, is_required, project_for_pippo).

prop(angular, is_required, project_for_region).
prop(angular, is_required, deployement_newere).

prop(junior_developer, work, project_for_pippo).
prop(cto, work, project_for_pippo).
prop(senior_developer, work, project_for_pippo).
prop(analist, work, project_for_pippo).
prop(team_leader, work, project_for_pippo).

prop(team_leader, work, application_enel).
prop(lead_developer, work, application_enel).
prop(backend_developer, work, application_enel).
prop(frontend_developer, work, application_enel).

prop(senior_developer, work, application_modis).
prop(co_founder, work, application_modis).
prop(cto, work, application_modis).
prop(scrum_master, work, application_modis).

prop(senior_developer, work, project_for_region).
prop(ceo, work, project_for_region).
prop(co_founder, work, project_for_region).
prop(junior_developer, work, project_for_region).
prop(frontend_developer, work, project_for_region).
prop(backend_developer, work, project_for_region).

prop(project_manager, work, project_for_university_of_bari).
prop(analist, work, project_for_university_of_bari).
prop(junior_developer, work, project_for_university_of_bari).
prop(developer, work, project_for_university_of_bari).

prop(co_founder, work, deployement_newere).
prop(project_manager, work, deployement_newere).
prop(frontend_developer, work, deployement_newere).
prop(backend_developer, work, deployement_newere).

prop(scrum_master, work, deployement_for_clobetasolo).
prop(junior_developer, work, deployement_for_clobetasolo).

prop(frontend_developer, work, project_for_fabio).
prop(junior_developer, work, project_for_fabio).
prop(analist, work, project_for_fabio).
prop(developer, work, project_for_fabio).


