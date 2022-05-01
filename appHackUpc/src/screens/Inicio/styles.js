import { StyleSheet } from 'react-native';

const styles = StyleSheet.create({
    container: {
        justifyContent: 'center',
        alignItems: 'center',
        height: 680,
        
    },
    button1: {
        marginHorizontal:65,
        justifyContent: 'center',
        alignItems: 'center',
        width: 250,
        height: 50 ,
        flexDirection: 'row',
        borderRadius: 25,
        backgroundColor: "#32427a",
        marginBottom: 30,
    },
    button2: {
        marginHorizontal:65,
        justifyContent: 'center',
        alignItems: 'center',
        width: 250,
        height: 50 ,
        flexDirection: 'row',
        borderRadius: 25,
        backgroundColor: "#32427a",
    },
    image: {
        flex: 1,
        height: 900,
        width: 500,
    },
});

export default styles;